Pay Close Attention to These

Important Reminder of Guidelines for Lemur Astrologer
As an attempter or reviewer you must go through this important checklist to ensure task quality in addition to existing guidelines present in the instructions or reviewer checklist.


1. Prompt Categorization:
Does the prompt match the difficulty level at the top of the task?
Yes, then proceed
No, then edit the difficulty field in the prompt categorization section
Does the sub-category of the prompt meet the requirements?
Yes, then proceed
No, then edit the sub-category field - we have to be strict here (i.e. Text to code should definitely be Text to code - just text in the prompt requesting a code output)

IMPORTANT: Simplified Example of this common sub-category error:
Task Category: Code Generation/Synthesis

Turn 1 Prompt: “Make a 2d minigolf game using JS”

Turn 1 Category: Text to Code (makes sense)

Turn 2 Prompt: “Additionally add a stopwatch to the top right corner”

Turn 2 Category: Text to Code (X this is bad, it should be Text to Code Edits, because we're asking for edits to existing code)

2. Code Testing:
If no rewrite is required (in the case of one good and one bad response), does the good response’s code run?
Yes, then proceed to step 4
No, then change the toggle to say a rewrite is required, and proceed to rewrite the response and proceed to step 4
Does the code run in the rewrites?
Yes, then proceed
No, then fix the code or SBQ
Is the code optimal and if code efficiency (i.e. O(n^2) vs O(1), etc) is described in the response, is it correctly described?  Make sure to verify.
Yes, then proceed
No, then update accordingly

3. Style and Presentation (Rewrite):
Does the code contain sufficient comments?
Yes, then proceed
No, then add comments
Does the rewritten response replace any paragraphs (especially those with at least 3 points) with bullet points instead?
Yes, then proceed
No, then re-word into three bullet points
Is all repetitive phrasing/wording removed?  Are repetitive statements removed and made more concise? (examples)
Yes, then proceed
No, then make the necessary edits
Is the tone aligned with the customer standards?
We should not have something like “Welcome to the world of VS Code!”  It should be concise and just straightforward/professional.  Avoid all pleasantries.
Yes, then proceed
No, then make the necessary edits

4. Instruction Following:

Does the rewritten response satisfy all of the requirements of the prompt?
Be like a lawyer when it comes to the prompt, for every ask or request in the prompt, does the rewritten response (or good response if no rewrite is required) satisfy it?
Yes, then proceed
No, then edit the rewrite further to make sure both the text and code address the prompt
Input validation (under the accuracy rating):
Is there any part of the code related to input handling? If so:
Are all data inputs being validated according to expectations?
Yes, then proceed.
No, then make the necessary edits.
Are all meaningful edge cases covered?
Yes, then proceed.
No, then correct the code as necessary.
