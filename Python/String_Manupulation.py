import textwrap

def slice_and_wrap_text(input_text, width):
    # Use textwrap to wrap the text to the specified width
    wrapped_text = textwrap.wrap(input_text, width)

    # Print each line of the wrapped text
    for line in wrapped_text:
        print(line)

if __name__ == "__main__":
    # Example input text
    input_text = "This is a long piece of text that we want to slice and wrap using textwrap module in Python. It helps in formatting the text to fit within a specified width."

    # Specify the width for wrapping
    wrap_width = 30

    # Call the function to slice and wrap the text
    slice_and_wrap_text(input_text, wrap_width)
