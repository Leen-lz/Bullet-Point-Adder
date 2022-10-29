# Uses pyperclip to utilize the system's clipboard
# Bullet points will be added to each copied line after run
import pyperclip


def bulletPointAdder():
    # paste the copied lines -> list
    text = pyperclip.paste()
    lines = text.split('\n')

    for i in range(len(lines)):
        lines[i] = '• ' + lines[i]

    # copy to Clipboard
    result = '\n'.join(lines)

    print(f"Copied to clipboard: \n{result} \n")
    pyperclip.copy(result)


if __name__ == '__main__':
    bulletPointAdder()
