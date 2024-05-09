def replace_emoji(input_text):
    emoji_dict = {
        ":thumbsup:": "👍",
        ":earth_asia:": "🌏",
        ":candy:": "🍬",
        ":ice_cream:": "🍨",
        ":1st_place_medal:": "🥇"
    }

    for emoji_code, emoji_char in emoji_dict.items():
        input_text = input_text.replace(emoji_code, emoji_char)

    return input_text

def main():
    usr_input = input("Input: ")

    replaced_input = replace_emoji(usr_input)

    print("Output:", replaced_input)

if __name__ == "__main__":
    main()
