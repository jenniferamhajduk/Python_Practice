def banner_text(text: str = " ", screen_width: int = 60) -> None:
    """
    Accepts the text in put and the screen width

    The function will asses whether the screen width is valid and will
    throw an error if the text exceeds the screen width - 4 

    :param The text and the screen width are passed into the function at invocation
    :raises valueError: If the supplied string is too long to fit
    :return The output of the text with the special formatting
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than the specified width {1}".format(text, screen_width))
    
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("there's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And...always look on the bright side of life...", 60)
banner_text("*", 60)