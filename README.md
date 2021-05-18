# Change Behaviour of Enter/Return/Space When Answer Shown

## Description
This add-on changes the behaviour of the ``Space``, ``Enter`` and ``Return`` key in the *answer* state from answering *Good* to either being ignored or reshowing the answer.

## Why
The gamepad button mappings on AnkiMobile has two functions that can be used to show the answer:

- "Show Answer/Answer Good": This is the behaviour of Anki 2.1 when pressing ``Space``, ``Enter`` or ``Return``. It shows the answer when the question is shown, and answers *Good* when the answer is shown.
- "Show Answer": It shows the answer when the question is shown, and when the answer is shown shows the answer again. 

I prefer the second option for two reasons:

- Not having two functions overloaded on the same button prevents accidental double taps from immediatly answering good. 
- Showing the answer again has a nice side effect: when audio is set to automatically play, it will replay the answer audio. The regular ``Replay Audio`` can be set to replay the question audio in answer. Therefore one has two options to replay audio: one with question (regular replay), and one with only the answer (the "Show Answer" shortcut).

On the Desktop version of Anki, there is no built-in option to only show the answer. ``Space``, ``Enter`` and ``Return`` will always not only show the answer, but also answer *Good*. This extension changes this behaviour. By default, pressing ``Space``, ``Enter`` or ``Return`` in the *answer*-state will reshow the answer, and therefore replay the audio. This can be changed in the configuration to completely ignore the key.

This extension was inspired by the add-on [*Ignore space/enter when answer shown*](https://ankiweb.net/shared/info/2160758119), which currently does not support Anki 2.1.x. If you find a bug or have a feature request, please report them on [on GitHub](https://github.com/baderj/anki-space-behaviour). 

## Usage
To change the behaviour of the ``Space`` /``Enter`` / ``Return`` key in *answer* mode go to *Tools > Add-ons > Anki Space Behaviour* and click *Config*. Set the ``mode`` to ``ignore`` when the keys should be ignored:

```
{
    "mode": "ignore"
}
```

and to ``show_answer`` when the answer should be shown again (triggering a replay of the answer audio files):

```
{
    "mode": "show_again"
}
```

