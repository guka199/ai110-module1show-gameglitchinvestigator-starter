# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
looks wise it was fine but I think hint of either going higher or lower appears every other try instead of every try
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  Hints were wrong and new game doesn't start at all

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
claude. I didn't write all #fixme logics. basically whatever problems I had I described it to claude and fixed it piece by piece.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
so my test file couldn't import my functions from logic_utils so it suggested me to use os to get correct path and it worked.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
for the tests it was looking for exact match instead of checking weather output string contained like win or higher and it would flag as a failed test when actual code was working fine

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
run and test all the bug fixes
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  checked correctnes of higher/lower hints.
- Did AI help you design or understand any tests? How?
yes it helped me design tests for new bug fixes

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

this was my first time using pytests and I will definitely try to use them in the future
