
# Chatbot (using RASA)

To create a chatbot to know about vehicle insurance policies , where users can login on website and be able to chat with the agent.
## Introduction

What is a CHATBOT ?

A chatbot or chatterbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent.
A chatbot is a type of software that can help customers by automating conversations and interact with them through messaging platforms.

What is RASA?

RASA is an open-source chatbot framework based on machine learning.


## How to get started 

To install the packages used inside the project , run the command below

```bash
  pip install -r requirements.txt
```

To Train model
```bash
  rasa run -m models --enable-api --cors "*"
```

To run chatbot on terminal
```bash
  rasa init
```
OR 
```bash
  rasa shell
```

## Documentation

[Chatbot notes](https://docs.google.com/document/d/1agGq9u-_Oeq92EDKrZaPtXWMV28EPkUL0_cySpLSl1M/edit?usp=sharing)

