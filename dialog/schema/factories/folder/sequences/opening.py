from dialog.schema.factories.action import GreetingAction
from dialog.schema.factories.grammar import GenericGrammar, FeelingGrammar

__author__ = 'robdefeo'


class OpeningSequences:
    @staticmethod
    def create():
        return {
            "@selectionType": "RANDOM",
            "@label": "OPENING SEQUENCES",
            (0, "input"): [
                {
                    (0, "grammar"): {
                        "item": [
                            "Hello",
                            "Hello again",
                            "hi there"
                        ]
                    },
                    (1, "action"): GreetingAction.create_increment(),
                    (2, "if"): [
                        {
                            (0, "cond"): {
                                "@varName": "Terminal_Exchange",
                                "@operator": "EQUAL_TO_YES"
                            },
                            (1, "goto"): {
                                "@ref": "output_welcome_back"
                            }
                        },
                        {
                            (0, "cond"): [
                                {
                                    "@varName": "Greeting_Count",
                                    "@operator": "GREATER_THEN",
                                    "#text": "2"
                                },
                                {
                                    "@varName": "Greeting_Count",
                                    "@operator": "GREATER_THEN",
                                    "#text": "2"
                                }
                            ],
                            (1, "goto"): {
                                "@ref": "output_end_of_small_talk"
                            }
                        }
                    ],
                    (3, "output"): {
                        (0, "prompt"): {
                            "item": [
                                "Hello.",
                                "Hi.",
                                "Hi there."
                            ],
                            "@selectionType": "RANDOM"
                        },
                        (1, "output"): {
                            "@id": "output_2459184",
                            (0, "prompt"): {
                                "item": [
                                    "How are you today?",
                                    "How are you feeling today?",
                                    "How is it going?"
                                ],
                                "@selectionType": "RANDOM"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): [
                                    {
                                        (0, "grammar"): {
                                            "item": [
                                                "Movies",
                                                "$ (GENRE)={Genre_Preference}",
                                                "$ (CERTIFICATION)={Certification_Preference}",
                                                "$ (RECENCY)={Recency_Preference}",
                                                "$ movies"
                                            ]
                                        },
                                        (1, "goto"): {
                                            "@ref": "input_2443892"
                                        }
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_not_so_good(),
                                        (1, "goto"): {
                                            "@ref": "output_sorry_to_hear_that"
                                        }
                                    },
                                    {
                                        (0, "grammar"): {
                                            "item": [
                                                "Not so bad",
                                                "$ not * bad"
                                            ]
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_good_to_hear"
                                        }
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_feeling_fine(),
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "Good to hear! <br> <br>",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_how_can_i_help_you"
                                            },
                                            "@id": "output_good_to_hear"
                                        }
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_feeling_great(),
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "Fantastic! So glad to hear it. <br> <br>",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_how_can_i_help_you"
                                            }
                                        }
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_feeling_bad(),
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "I'm sorry to hear that. <br> <br>",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_how_can_i_help_you"
                                            },
                                            "@id": "output_sorry_to_hear_that"
                                        }
                                    }
                                ],
                                (1, "goto"): {
                                    "@ref": "search_2414738"
                                }
                            }
                        }
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "How are you",
                            "$ how have you been doing",
                            "$ how is it going",
                            "$ how are you",
                            "$ what's shaking",
                            "$ what's up"
                        ]
                    },
                    (1, "action"): GreetingAction.create_increment(),
                    (2, "if"): {
                        (0, "cond"): [
                            {
                                "@varName": "Greeting_Count",
                                "@operator": "GREATER_THEN",
                                "#text": "2"
                            },
                            {
                                "@varName": "Greeting_Count",
                                "@operator": "GREATER_THEN",
                                "#text": "2"
                            }
                        ],
                        (1, "output"): {
                            "@id": "output_end_of_small_talk",
                            (0, "prompt"): {
                                "item": "You're very polite, but don't you want me to look up movies for you?",
                                "@selectionType": "RANDOM"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): [
                                    {
                                        (0, "grammar"): GenericGrammar.create_yes(),
                                        (1, "goto"): {
                                            "@ref": "output_ask_for_recency"
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.create_no(),
                                        (1, "action"): GreetingAction.create_reset(),
                                        (2, "output"): {
                                            "prompt": {
                                                "item": "Okay, fine.",
                                                "@selectionType": "RANDOM"
                                            }
                                        }
                                    },
                                    {
                                        (0, "grammar"): {
                                            "item": "Okay"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_ask_for_recency"
                                        }
                                    }
                                ],
                                (1, "goto"): {
                                    "@ref": "search_2414738"
                                }
                            }
                        }
                    },
                    (3, "input"): {
                        (0, "grammar"): {
                            "item": [
                                "Fine",
                                "$ excellent",
                                "$ outstanding",
                                "$ fabulous",
                                "$ terrific",
                                "$ not good",
                                "$ not so good",
                                "$ not well",
                                "$ not so well",
                                "$ terrible",
                                "$ awful",
                                "$ worst",
                                "$ bored",
                                "$ sad",
                                "$ good",
                                "$ well",
                                "$ fine",
                                "$ thirsty",
                                "$ hungry",
                                "$ tired"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "I am doing well, thanks."
                            },
                            (1, "goto"): {
                                "@ref": "output_how_can_i_help_you"
                            }
                        }
                    },
                    (4, "output"): {
                        (0, "prompt"): {
                            "item": "I am doing well, thanks."
                        },
                        (1, "goto"): {
                            "@ref": "output_2459184"
                        }
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "Nice to meet you",
                            "$ nice to meet you",
                            "$ pleasure to meet you",
                            "$ make your acquaintance"
                        ]
                    },
                    (1, "if"): {
                        (0, "cond"): {
                            "@varName": "Greeting_Count",
                            "@operator": "GREATER_THEN",
                            "#text": "2"
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "You're very polite, but don't you want me to look up movies for you?"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): [
                                    {
                                        (0, "grammar"): GenericGrammar.create_yes(),
                                        (1, "goto"): {
                                            "@ref": "output_ask_for_recency"
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.create_no(),
                                        (1, "action"): GreetingAction.create_reset(),
                                        (2, "output"): {
                                            "prompt": {
                                                "item": "Okay, fine."
                                            }
                                        }
                                    },
                                    {
                                        (0, "grammar"): {
                                            "item": "Okay"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_ask_for_recency"
                                        }
                                    }
                                ],
                                (1, "goto"): {
                                    "@ref": "search_2414738"
                                }
                            }
                        }
                    },
                    (2, "output"): {
                        (0, "prompt"): {
                            "item": "Nice to meet you too, {User_Name}!",
                            "@selectionType": "RANDOM"
                        },
                        (1, "goto"): {
                            "@ref": "output_how_can_i_help_you"
                        }
                    }
                }
            ]
        }