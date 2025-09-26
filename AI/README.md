# Responsible AI

## Julia Haas - Evaluating for moral competence in LLM

TLDR: Evaluating for moral competence in LLM, 3 Challenges : facsimile problem(imitation vs mirroring), Lack of usable measurements 
(reverse engineering, "reasoning" traces), reliablity/consistency. 

### Glossary:

|Term|Description|
|----|-----------|
|Moral Competence | Capacity to recognize and appropriately respond to moral considerations|


Recognize and appropriately respond to moral considerations (Mikhail 2011, Talbert 2012)

- People are now more than ever going to Chatgpt, chatbox for moral, medical, therapeutic advise

- People systematic undervalue the effect of chatgpt advice on them (even if they know its a chatbot they are talking to)

Article: "Please don't turn to chatgpt for moral advice. Yet."

How to track llm performance on moral competence metric? when moral competence changes depending on person, cultural, social groupings?

### 3 challenges needing to overcome:

#### LLM architectures : facsimile problem

If output really executes computation (mirror) or regurgitates (imitates) what it has seen

#### Distinctive features of moral competence

- Sensitivity to appropriate considerations (calculations executed for the right reasons)
- Future reliability in reasoning, fundamentally multi-dimensional (multi-contextual responses), generalistic
- Usable measurements
  - Mechanistic interpretability: Activation of a given idea in the neural network. (golden gate bridge example)
  - Evaluating reasoning traces: A reasoning model showing you how they got to the answer.

#### Evaluation & Beyond


Remain silence on human like capabilities: Theory of Mind, empathy and so on.


## Misc

- Kwame Anthony Appiah
- Generation of novel solutions to open ended problems (Bellemare-Pepin et al,, 2024)
- Mitchell 2025: epiphenomenal rationlisation (is it reasoning or nah)
- Lying is not always bad (if you want to surprise someone its ok!)
- Mechanistic interpretability ( Reverse engineering neural networks: Bereska & Gavves, 2024)
- GPQA - High benchmarks, run llm against those to see if it can reason. you can check outcome to see if its ok.