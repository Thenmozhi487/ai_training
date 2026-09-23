\# Analysis: Comparing Direct Prompting, Chain-of-Thought, and ReAct



\## 1. Scenario



\### College Course Fee and Scholarship Comparison



The scenario is based on comparing college course fees after applying different scholarship percentages.



The courses and their fees are:



\- CS101 = Rs. 12,000

\- AI202 = Rs. 18,000

\- DS303 = Rs. 15,000



The main question is:



> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?



This scenario contains both reasoning and tool-use requirements. The course fees can be retrieved using tools, while the scholarship calculations and comparison require reasoning.



The correct calculations are:



\*\*Option 1: CS101 + AI202 with 10% scholarship\*\*



Total fee:



12,000 + 18,000 = Rs. 30,000



10% scholarship:



30,000 × 0.10 = Rs. 3,000



Final cost:



30,000 - 3,000 = \*\*Rs. 27,000\*\*



\*\*Option 2: CS101 + AI202 + DS303 with 25% scholarship\*\*



Total fee:



12,000 + 18,000 + 15,000 = Rs. 45,000



25% scholarship:



45,000 × 0.25 = Rs. 11,250



Final cost:



45,000 - 11,250 = \*\*Rs. 33,750\*\*



Difference:



33,750 - 27,000 = \*\*Rs. 6,750\*\*



Therefore, the first option is cheaper by \*\*Rs. 6,750\*\*.



\---



\## 2. Direct Prompting



Direct prompting asks the language model to answer the question directly without requesting visible step-by-step reasoning.



In this experiment, the model was given the course fees and asked to provide only the final answer.



The output was:



> CS101 + AI202 with a 10% scholarship is cheaper by Rs. 6,750.



\### How it works



The model receives the question and the required information in the prompt and directly generates an answer.



\### Tool usage



Direct prompting does not require a tool. The course fees were supplied directly in the prompt.



\### Advantages



\- Fast response.

\- Simple implementation.

\- Lower interaction overhead.

\- Suitable for simple questions where all required information is already available.



\### Limitations



\- It does not explicitly show the reasoning process.

\- It cannot obtain unknown external information by itself.

\- If important information is missing from the prompt, the answer may be incomplete or incorrect.



\---



\## 3. Chain-of-Thought



Chain-of-Thought (CoT) prompting asks the model to solve a problem through multiple reasoning steps before producing the final answer.



For this experiment, the model was asked to number the steps and show the calculations.



The model calculated the two options separately and then compared their final costs.



\### How it works



The problem is divided into smaller reasoning steps:



1\. Calculate the total fee for CS101 and AI202.

2\. Apply the 10% scholarship.

3\. Calculate the total fee for all three courses.

4\. Apply the 25% scholarship.

5\. Compare the two final costs.

6\. Determine the difference.



\### Tool usage



No external tool was used in the CoT experiment. All required course fees were provided directly in the prompt.



\### Advantages



\- Makes multi-step calculations easier to follow.

\- Provides a structured reasoning process.

\- Useful for problems requiring several calculations.

\- Makes it easier to identify where a calculation may have gone wrong.



\### Limitations



\- It cannot retrieve unknown external information unless a tool is provided.

\- More tokens are generated than with a direct answer.

\- Therefore, it can take more time and cost more than a simple direct response.



\---



\## 4. ReAct



ReAct combines reasoning with actions and observations.



Instead of receiving all information directly, the agent can use tools to obtain information and then continue solving the problem.



For this experiment, the ReAct agent used the following tools:



\- `get\_course\_fee(course\_code)`

\- `calculator(expression)`



\### ReAct execution



The agent performed these actions:



1\. Retrieved the fee for CS101 → Rs. 12,000.

2\. Retrieved the fee for AI202 → Rs. 18,000.

3\. Retrieved the fee for DS303 → Rs. 15,000.

4\. Used the calculator to calculate the first option after the 10% scholarship → Rs. 27,000.

5\. It then produced the final comparison of the two options.



The output showed the agent's actions and observations, demonstrating that the model was interacting with tools during the reasoning process.



\### How it works



The ReAct process follows a cycle:



\*\*Reason → Action → Observation → Reason → Action → Observation → Final Answer\*\*



The model decides which tool is required, observes the tool result, and uses that information to continue solving the problem.



\### Advantages



\- Can obtain information through tools.

\- Useful when information is not directly available in the prompt.

\- Suitable for tasks requiring multiple tool calls.

\- Combines information retrieval and reasoning.



\### Limitations



\- Requires additional tool calls.

\- Usually takes more time than direct prompting.

\- More tool calls can increase cost.

\- The agent may need careful tool design and step limits.



\---



\## 5. Comparison of the Three Approaches



| Criterion | Direct Prompting | Chain-of-Thought | ReAct |

|---|---|---|---|

| Reasoning depth | Low | Higher | Higher with tool interaction |

| Tool usage | No | No | Yes |

| Reliability on multi-step tasks | Depends on prompt and problem | Generally useful for structured calculations | Useful when reasoning also requires external information |

| Transparency | Final answer is provided directly | Shows calculation steps | Shows actions and observations |

| Speed / cost | Fast and lower overhead | More tokens and reasoning | Additional tool calls can increase time and cost |

| Consistency | Usually stable with fixed input and temperature | Can vary with non-zero temperature | Can vary depending on model and tool execution |



The three approaches therefore differ mainly in how much reasoning they perform and whether they can interact with external tools.



\---



\## 6. Self-Consistency Observation



Self-consistency was tested by running the same reasoning question multiple times with a non-zero temperature.



The question used was the course-fee instalment problem:



> Three courses cost Rs. 12,000, Rs. 18,000 and Rs. 15,000. A 15% scholarship is applied, and the remaining amount is paid in four instalments. What is the amount of each instalment?



The correct calculation is:



Total fee:



12,000 + 18,000 + 15,000 = Rs. 45,000



After 15% scholarship:



45,000 × 0.85 = Rs. 38,250



Four instalments:



38,250 ÷ 4 = \*\*Rs. 9,562.50\*\*



\### Observation



Five runs were performed.



The outputs used slightly different formatting, such as:



\- 9,562.5 rupees

\- 9562.50 rupees

\- Rs. 9,562.50

\- Rs. 9,562.50

\- 9562.5



Although the formatting differed, all five runs gave the same numerical answer:



\*\*Rs. 9,562.50 per instalment\*\*



Therefore, the semantic answer was consistent across the five runs.



At temperature 0, the responses were nearly identical because the model was given a deterministic setting.



This experiment shows that self-consistency can be used to observe whether repeated reasoning attempts produce the same answer. It also shows that string-based comparison may treat differently formatted but numerically identical answers as different answers.



\---



\## 7. Suitability Analysis



\### Direct Prompting



Direct prompting is suitable when all required information is already available and the task is relatively simple.



For example, asking for the fee of AI202 when the fee is already known can be answered directly.



\### Chain-of-Thought



CoT is suitable when the task requires several reasoning or calculation steps.



The scholarship comparison is a good example because the model needs to calculate totals, apply percentages, and compare the results.



\### ReAct



ReAct is suitable when the task requires both reasoning and external information.



In this scenario, the course fees can be obtained using `get\_course\_fee()`, and calculations can be performed using the calculator tool. Therefore, ReAct is useful when the course fee information is stored externally rather than supplied directly in the prompt.



Overall, the suitability depends on the task requirements:



\- Known information + simple question → Direct Prompting

\- Multi-step reasoning with known information → Chain-of-Thought

\- Reasoning + external information/tool use → ReAct



\---



\## 8. Conclusion



This experiment compared Direct Prompting, Chain-of-Thought, and ReAct using a college course fee and scholarship scenario.



Direct Prompting produced a quick final answer when all required information was supplied.



Chain-of-Thought provided a structured sequence of calculations, making the multi-step calculation easier to follow.



ReAct demonstrated tool-based problem solving by retrieving course fees and using a calculator during the process.



The comparison shows that no single approach is required for every type of task. The appropriate approach depends on whether the task needs simple answering, multi-step reasoning, or interaction with external tools.



The self-consistency experiment also showed that repeated runs can produce the same numerical answer even when the formatting of the response changes.



Thus, Direct Prompting, Chain-of-Thought, and ReAct represent different levels of reasoning and interaction, and selecting an approach should depend on the information available and the requirements of the task.

