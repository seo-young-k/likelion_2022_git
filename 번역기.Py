from googletrans import Translator

translator = Translator()

sentence = input("문장을 입력해주세요: ")

result = translator.translate(sentence,'en')
detected = translator.detect(sentence)

print("=======출 력 결 과=======")
print(detected.lang,':',sentence)
print(result.dest,":",result.text)
print("====================")

