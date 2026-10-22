#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upward Communication Copilot - 30-Second Async Executive Brief Generator
Run: python cli/executive_brief_generator.py --generate-sample
"""

import sys
import argparse
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BANNER = """
======================================================================
   UPWARD COMMUNICATION COPILOT // 30S ASYNC EXECUTIVE GENERATOR
   Grounded in Tencent WeChat Pay Senior Management Methodologies
======================================================================
"""

SAMPLE_PASSIVE = """
Leader, the upstream API team suddenly had a bug today, so our project cannot proceed as scheduled. What should we do now? When can they fix it?
"""

SAMPLE_EXECUTIVE = """
[TL;DR / STATUS]: [AT RISK] -- Core payment flow blocked by upstream auth API failure; fallback activated to protect launch date.
[BUSINESS METRIC]: $1.2M daily GMV launch at risk; 4-hour delay tolerated before customer impact.
[DECISION FORK]: Need authorization by 16:00 today between two mitigation paths:
  * Option A (Recommended): Switch traffic to shadow secondary auth gateway. Zero customer downtime; increases cloud egress cost by $450.
  * Option B (Conservative): Pause rollout and wait for upstream hotfix by 20:00. Pushes go-live to tomorrow; zero monetary cost.
[NEXT STEPS & DRI]: Testing Option A in staging now. DRI: Alex (Lead Architect). Next broadcast at 15:30.
"""

def generate_sample():
    print(BANNER)
    print("Testing contrast: Junior Panic Message vs. Executive 30-Second Async Brief\n")
    
    print("--- 1. Junior Passive Message (Dumps Problem on Leader) ---")
    print(f'"{SAMPLE_PASSIVE.strip()}"')
    print("-> Manager Reaction: Anxiety, friction, forced to step in as micro-manager.\n")

    time.sleep(0.3)

    print("--- 2. Executive 30-Second Async Brief (Options-First Alignment) ---")
    print(SAMPLE_EXECUTIVE.strip())
    print("\n-> Manager Reaction: Immediate clarity, selects Option A in 10 seconds, zero surprise.\n")
    print("======================================================================")
    print("Rule: Never bring questions to leadership without options and trade-offs.")
    print("======================================================================")

def main():
    parser = argparse.ArgumentParser(description="Executive Brief Generator")
    parser.add_argument("--generate-sample", action="store_true", help="Generate comparative executive broadcast")
    args = parser.parse_args()

    if args.generate_sample or len(sys.argv) == 1:
        generate_sample()

if __name__ == "__main__":
    main()
