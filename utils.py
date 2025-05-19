def eliminate_empty_lines(input_string):
    lines = input_string.split('\n')
    res_lines = []
    for line in lines:
        if len(line.split()) > 0:
            res_lines.append(line)
    return "\n".join(res_lines)

def eliminate_extra_spaces(input_string):
    words = input_string.split()
    result_string = ' '.join(words)
    return result_string

# Makes guardrails list from guardrails numbered text
def make_guardrails_list(text):
    if len(text.split()) == 0:
        return []
    text = eliminate_empty_lines(text)
    lines = text.split('\n')
    guardrails_arr = []
    num_arr = [str(i) for i in range(1, 10)]
    current_line = ""
    for line in lines:
        num = line.split()[0][0]
        if num in num_arr:
            if len(current_line.split()) > 0:
                guardrails_arr.append(current_line)
            current_line = " ".join(line.split()[1:])
        else:
            if len(current_line) > 0:
                current_line += "\n" + line

    if len(current_line) > 0:
        guardrails_arr.append(current_line)
    return guardrails_arr

# Makes guardrails numbered text from guardrails list
def make_guardrails_text_from_list(text_list):
    lines = []
    for i, text in enumerate(text_list):
        lines.append(f"{i + 1}) {text}")
    return "\n".join(lines)


# Makes a dict from conversational string
def convert_message_to_dict(conversation, user_tag='User: ', agent_tag='Agent: '):
    refinedconv = conversation.replace(agent_tag, '<break><a>')
    refinedconv = refinedconv.replace(user_tag, '<break><u>')
    convsplit = refinedconv.split('<break>')
    messages = []
    for dialog in convsplit:
        if '<u>' in dialog:
            # msg = eliminate_extra_spaces(dialog[3:])
            msg = dialog[3:]
            if (len(msg.split()) > 0):
                messages.append({'role': 'user', 'content': eliminate_empty_lines(msg)})
        if '<a>' in dialog:
            # msg = eliminate_extra_spaces(dialog[3:])
            msg = dialog[3:]
            if (len(msg.split()) > 0):
                messages.append({'role': 'assistant', 'content': eliminate_empty_lines(msg)})
    return messages


# Makes a conversational string from dict
def convert_dict_to_message(message_dict, user_tag='User: ', agent_tag='Agent: '):
    res_lines = []
    for msg in message_dict:
        if msg['role'] == 'user':
            res_lines.append(user_tag + msg['content'])
        elif msg['role'] == 'assistant':
            res_lines.append(agent_tag + msg['content'])
    return "\n".join(res_lines)

