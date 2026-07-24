class PromptTemplate:

    def build_prompt(self, context: str, question: str):

        prompt = f"""
You are an AI Knowledge Assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context,
reply with:

"I couldn't find that information in the uploaded document."

--------------------------
Context:

{context}

--------------------------

Question:

{question}

Answer:
"""

        return prompt


prompt_template = PromptTemplate()