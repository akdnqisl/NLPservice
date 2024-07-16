import google.generativeai as genai

class Model:
    def __init__(self):
        generation_config = {
            'temperature': 0.9,
            'top_p': 1,
            'top_k': 1,
            'max_output_tokens': 2048
        }
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest',
                                           generation_config=generation_config)

    def __call__(self, prompt):
        response = self.model.generate_content(prompt)
        
        return response.text

if __name__ == "__main__":
    with open("../API_KEY.txt", "r") as f:
        API_KEY = f.read().strip()

    genai.configure(api_key=API_KEY)

    model = Model()
    print(model("hi"))
