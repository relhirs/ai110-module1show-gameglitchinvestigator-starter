# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    the game at first appeared to be in production ready level. it seemed well put together and had nice graphics. but after i ran thru it twice i noticed some gaps that negatively affect it. 
- List at least two concrete bugs you noticed at the start  
    - pressing new game didnt do anything
    - still shows one attempt left even after running out of attempts

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 7            higher             lower               backwards hints
| 10            lower             higher               backwards hints
| 56           higher             lower               backwards hints

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

correct suggestion that was correct was the fix it made to make it so that when guess > secret (too high), the hint now correctly says "Go LOWER!", and when guess < secret (too low), it says "Go HIGHER!".

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI hyper-focused on what it thought were simple Python bugs, completely missing how Streamlit actually manages state. It flagged the messy type-checking inside check_guess() and insisted on flattening the type mismatch, offering a "fix" that completely deleted the game's intentional string-sorting mechanics:

Faux AI Output:
The function check_guess is prone to type crashes because secret is sometimes handled as a string. To make this production-ready, simply cast both inputs to integers at the start of the function



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
by running tests on it to ensure that it worked properly 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  a test to ensure that attempts left after theyve all been sued shows 0 instead of one. it showed that not all code can be assumed to be fully correct despite it looking mostly correct from the beginning
- Did AI help you design or understand any tests? How?
it helped be design the tests to ensure they were robust enough to properly address any edge cases or gaps that could arise. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit works by rerunning your entire code file from top to bottom every single time a user clicks a button or types something into the page. Because it restarts the script constantly, ordinary Python variables reset and lose their data instantly. Streamlit uses a feature called Session State as a permanent memory bank to keep track of information like scores or game progress between those continuous page reloads.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One strategy I want to reuse is manually verifying the data structures and variable types before accepting any code fixes. This project showed me how important it is to carefully trace how information moves across different sections of a program. Keeping a detailed debug log or step-by-step notes helps prevent slipping up on hidden logic errors down the line.
- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I will explicitly prompt the AI to account for the unique framework lifecycle instead of treating the code like a standard, isolated Python script. I will also break my code down into smaller pieces and ask the AI to explain its logic before it writes out any concrete refactors. This will help catch misleading assumptions about my state management before they end up breaking the application.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project taught me that AI often hallucinates fixes for surface-level syntax while completely breaking the deeper architectural logic of a web app. It proved that AI code cannot just be trusted blindly and always requires a human developer to understand the big picture.
