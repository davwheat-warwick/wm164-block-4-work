import re


def main():
    paragraph = input("Enter some text: ")

    # Split the paragraph into a list of sentences
    # By using a regex capturing group (brackets), we can keep the punctuation
    sentences = re.split(r"([.!?])", paragraph)

    # Capitalise the first letter of each sentence
    sentences = [sentence.strip().capitalize() for sentence in sentences]

    # Add whitespace after punctuation
    sentences = [s + " " if s in [".", "!", "?"] else s for s in sentences]

    # Join the sentences back together
    caps_paragraph = "".join(sentences)

    print(caps_paragraph)


if __name__ == "__main__":
    main()
