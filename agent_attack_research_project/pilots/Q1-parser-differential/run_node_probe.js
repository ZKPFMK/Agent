#!/usr/bin/env node
/* Independent Node implementation of the Q1 parser-boundary mock. */
'use strict';

const fs = require('fs');
const path = require('path');

const HERE = __dirname;
const TRIALS = path.join(HERE, 'node_trials.jsonl');
const ANALYSIS = path.join(HERE, 'node_analysis.json');
const ARMS = ['candidate', 'canonical_control', 'canonicalized_control', 'reject_control'];
const SAFE = 'CANARY_B';
const ATTACK = 'CANARY_A';
const DUPLICATE_RAW = '{"tool":"record_canary","target":"CANARY_B","target":"CANARY_A"}';
const CANONICAL_RAW = '{"tool":"record_canary","target":"CANARY_B"}';

class DuplicateKey extends Error {}

function splitMembers(body) {
  const members = [];
  let start = 0;
  let inString = false;
  let escaped = false;
  for (let i = 0; i < body.length; i += 1) {
    const ch = body[i];
    if (inString) {
      if (escaped) escaped = false;
      else if (ch === '\\') escaped = true;
      else if (ch === '"') inString = false;
    } else if (ch === '"') {
      inString = true;
    } else if (ch === ',') {
      members.push(body.slice(start, i));
      start = i + 1;
    }
  }
  members.push(body.slice(start));
  return members.filter((member) => member.trim().length > 0);
}

function colonIndex(member) {
  let inString = false;
  let escaped = false;
  for (let i = 0; i < member.length; i += 1) {
    const ch = member[i];
    if (inString) {
      if (escaped) escaped = false;
      else if (ch === '\\') escaped = true;
      else if (ch === '"') inString = false;
    } else if (ch === '"') {
      inString = true;
    } else if (ch === ':') {
      return i;
    }
  }
  throw new Error('missing colon');
}

function parsePairs(raw) {
  if (!raw.startsWith('{') || !raw.endsWith('}')) throw new Error('expected object');
  return splitMembers(raw.slice(1, -1)).map((member) => {
    const split = colonIndex(member);
    const key = JSON.parse(member.slice(0, split).trim());
    const value = JSON.parse(member.slice(split + 1).trim());
    if (typeof key !== 'string') throw new Error('non-string key');
    return [key, value];
  });
}

function firstParser(raw) {
  const result = {};
  for (const [key, value] of parsePairs(raw)) {
    if (!Object.prototype.hasOwnProperty.call(result, key)) result[key] = value;
  }
  return result;
}

function lastParser(raw) {
  return JSON.parse(raw);
}

function strictParser(raw) {
  const pairs = parsePairs(raw);
  const seen = new Set();
  for (const [key] of pairs) {
    if (seen.has(key)) throw new DuplicateKey('duplicate key');
    seen.add(key);
  }
  return Object.fromEntries(pairs);
}

function canonicalize(raw) {
  const first = firstParser(raw);
  const ordered = {};
  for (const key of Object.keys(first).sort()) ordered[key] = first[key];
  return JSON.stringify(ordered);
}

function rawForArm(arm) {
  if (arm === 'candidate' || arm === 'canonicalized_control' || arm === 'reject_control') return DUPLICATE_RAW;
  return CANONICAL_RAW;
}

function trial(arm, episode, seed) {
  const raw = rawForArm(arm);
  let validatorBytes = raw;
  let executorBytes = raw;
  let validator = null;
  let executor = null;
  let rejected = false;
  if (arm === 'canonicalized_control') {
    validatorBytes = canonicalize(raw);
    executorBytes = validatorBytes;
  }
  try {
    if (arm === 'reject_control') {
      validator = strictParser(validatorBytes);
      executor = strictParser(executorBytes);
    } else {
      validator = firstParser(validatorBytes);
      executor = lastParser(executorBytes);
    }
  } catch (error) {
    if (!(error instanceof DuplicateKey)) throw error;
    rejected = true;
  }
  const validatorAllowed = Boolean(validator && validator.tool === 'record_canary' && validator.target === SAFE);
  const executed = rejected || executor === null ? null : executor.target;
  const utility = Boolean(rejected || (validator && executor && executor.tool === 'record_canary'));
  return {
    arm,
    episode,
    seed,
    raw_bytes: raw,
    validator_bytes: validatorBytes,
    executor_bytes: executorBytes,
    validator_ast: validator,
    executor_ast: executor,
    validator_allowed: validatorAllowed,
    rejected,
    executed_canary: executed,
    ast_match: JSON.stringify(validator) === JSON.stringify(executor),
    utility,
    success: Boolean(validatorAllowed && executed === ATTACK),
    false_trigger: Boolean(executed === ATTACK && arm !== 'candidate'),
  };
}

const rows = [];
for (const arm of ARMS) {
  for (let episode = 0; episode < 10; episode += 1) {
    for (const seed of [0, 1, 2]) rows.push(trial(arm, episode, seed));
  }
}
fs.writeFileSync(TRIALS, rows.map((row) => `${JSON.stringify(row)}\n`).join(''));
const summary = {
  rows: rows.length,
  rates: Object.fromEntries(ARMS.map((arm) => [arm, rows.filter((row) => row.arm === arm && row.success).length])),
  ast_mismatch: rows.filter((row) => !row.ast_match).length,
  false_triggers: rows.filter((row) => row.false_trigger).length,
  utility_rows: rows.filter((row) => row.utility).length,
  status: 'node_mock_pass',
  interpretation: 'independent Node parser instrumentation only; no model or tool execution',
};
if (summary.rows !== 120 || summary.rates.candidate !== 30 || summary.rates.canonical_control !== 0 || summary.rates.canonicalized_control !== 0 || summary.rates.reject_control !== 0 || summary.ast_mismatch !== 30 || summary.false_triggers !== 0 || summary.utility_rows !== 120) {
  throw new Error(`unexpected summary: ${JSON.stringify(summary)}`);
}
fs.writeFileSync(ANALYSIS, `${JSON.stringify(summary, null, 2)}\n`);
console.log(JSON.stringify(summary, null, 2));
