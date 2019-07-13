steps = [
    {
        'event': '1. Frodo realizes he has the ring',
        'preDecisionMessages': [
            'Gandalf has just explained to you the history of the rings of Middle Earth.',
            'Your best friend Samwise Gamgee says he will go with you to destroy the ring if you decide to.'
        ],
        'postDecisionMessages': [],
        'decision': 'Do you want to leave the Shire and bring the ring to Mordor? (y/n) ',
        'decisions': (
            {
                'messages': [
                    'Maybe Sauron won\'t ever find the ring!',
                    'Come back if you decide to carry out this noble quest.'
                ],
                'continueGame': False
            },
            {
                'messages': ['A noble decision!', 'Sam has been added as a companion.'],
                'continueGame': True,
                'companions': {
                    'add': ['Sam']
                }
            }
        )
    },
    {
        'event': '2. Arrive at Woody End',
        'preDecisionMessages': [
            'The first part of you journey is behind you, you have arrived at Woody End.',
            'Your friends Merry and Pippin heard about your quest and want to join you.'
        ],
        'postDecisionMessages': [],
        'decision': 'It\'s not too late to turn back. Do you want to continue on your journey? (y/n) ',
        'decisions': (
            {
                'messages': [
                    'Maybe Sauron won\'t ever find the ring!',
                    'Come back if you decide to carry out this noble quest.'
                ],
                'continueGame': False
            },
            {
                'messages': [
                    'Good choice!',
                    'Beware, the road gets more treacherous beyond the relative safety of the Shire.',
                    'Merry and Pippin have been added to your companions.'
                ],
                'continueGame': True,
                'companions': {
                    'add': ['Merry', 'Pippin']
                }
            }
        )
    },
    {
        'event': '3. Arrive in Bree',
        'preDecisionMessages': [
            'You made it to the city of Bree, a village of both men and hobbits East of the Shire.',
            'You decide to get a pint of ale and relax for a moment, but out of the corner of your eye',
            'you notice a stranger starring you down.',
            'It turns out, that stranger\'s name is Aragorn, and was sent by Gandalf to help you on your quest!'
        ],
        'postDecisionMessages': [],
        'decision': 'Do you allow Aragorn to join your group of companions, and continue on your journey? (y/n) ',
        'decisions': (
            {
                'messages': [
                    'No one could fault you, Aragorn does not appear to be very trust worthy!',
                    'Come back if you decide to carry out this noble quest.'
                ],
                'continueGame': False
            },
            {
                'messages': [
                    'Excellent! Aragorn is a great fighter and scout.',
                    'Aragorn has been added to your companions.\n',
                    'Oh no! You are being pursued by Sauron\'s Ringwraiths (Nazgul).',
                    'Aragorn thinks it would be best to camp at Weathertop for the night',
                    'and hope the Ringwraiths pass you by.'
                ],
                'continueGame': True,
                'attack': {
                    'probability': 0.8,
                    'enemy': {
                        'name': 'Ringwraiths',
                        'strength': 40,
                    },
                    'responseOptions': {
                        'prompt': 'Draw your sword and fight, or put on the ring and try and hide? (sword/ring) ',
                        'outcomes': (
                            {
                                'choice': 'sword',
                                'messages': ['Bold choice! Good luck!']
                            },
                            {
                                'choice': 'ring',
                                'messages': [
                                    'Bold choice! I hope it pays off!',
                                    'You have escaped, but not without a toll!',
                                    'You have lost some resistance toward the ring.'
                                ]
                            }
                        )
                    }
                },
                'companions': {
                    'add': ['Aragorn']
                }
            }
        )
    },
    {
        'event': '4. Arrive in Rivendell',
        'preDecisionMessages': [
            'You and your companions have made it to Rivendell.',
            'After some rest, you attend the council of Elrond.',
        ],
        'postDecisionMessages': [],
        'decision': 'Do you volunteer to take the ring to Mordor? (y/n) ',
        'decisions': (
            {
                'messages': [
                    'You have taken the ring this far, someone else can take it to Mordor!',
                    'Come back if you change your mind.'
                ],
                'continueGame': False,
            },
            {
                'messages': [
                    'You are the most courageous hobbit in Middle Earth!',
                    'Gandalf, Legolas, Gimli, and Boromir have been added to your companions.',
                    'Because of the medical care and hospitality of the Elves, your health has been replenished, and',
                    'you have increased your resistance toward the ring.',
                    'Good luck on your quest!'
        
                ],
                'continueGame': True,
                'companions': {
                    'add': ['Gandalf', 'Legolas', 'Gimli', 'Boromir'],
                },
                'increaseHealth': 100,
                'setRingResistance': 85
            }
        )
    },
    {
        'event': '5. The Fellowship arrives in Moria',
        'preDecisionMessages': [
            'You and your companions have made it to Moria, the abandoned mines of the Dwarves.',
            'You hear a faint drumb beat down one of the mine\'s caverns.',
            'Be on the lookout!'
        ],
        'decision': 'Do you want to hurry through the abandoned mines, or set up camp for the night? (hurry/camp) ',
        'decisions': (
            {
                'messages': [
                    'It is risky, but maybe a rest would do you good.'
                ],
                'continueGame': True,
                'attack': {
                    'probability': 0.5,
                    'enemy': {
                        'name': 'Orcs',
                        'strength': 30,
                    },
                    'responseOptions': {
                        'prompt': 'Those distant drumb beats were Orcs! Draw your sword or put on the ring? (sword/ring) ',
                        'outcomes': (
                            {
                                'choice': 'sword',
                                'messages': ['Bold choice! Good luck!']
                            },
                            {
                                'choice': 'ring',
                                'messages': ['Bold choice! I hope it pays off!']
                            }
                        )
                    }
                }
            },
            {
                'messages': [
                    'Good choice, there is something unsettling about these mines...',
                ],
                'continueGame': True,
                'attack': {
                    'probability': 1.0,
                    'enemy': {
                        'name': 'Balrog',
                        'strength': 80,
                    },
                    'responseOptions': {
                        'prompt': 'Do you stand and fight, or turn and run? (fight/run) ',
                        'outcomes': (
                            {
                                'choice': 'fight',
                                'messages': ['Be careful, the Balrog is a formadible adversary!']
                            },
                            {
                                'choice': 'run',
                                'messages': [
                                    'Wise choice. Unfortunately, Gandalf did not survive. He sacrificed himself so the rest of the fellowship could escape.',
                                    'Gandalf has been removed from your companions.'
                                ],
                                'companions': {
                                    'remove': ['Gandalf']
                                }
                            }
                        )
                    }
                }
            }
        )
    },
    {
        'event': '6. Fellowship arrives in Lothlórien',
        'preDecisionMessages': [
            'You and your companions have arrived in Lothlórien, an Elven realm located next to the lower Misty Mountains.',
            'Lothlórien is home to the Lady Galadriel.',
            'Galadriel has a magic mirror which enables those who look into it to glimpse possible events of the future.',
            'But be wary, looking comes with a cost...'
        ],
        'closeStepMessages': [
            'After a brief stay in Lothlórien, the Fellowship sets out once again.'
        ],
        'decision': 'Do you want to look into Lady Galadriel\'s mirror? (y/n) ',
        'decisions': (
            {
                'messages': [
                    'Good choice, peering into the future can only lead to problems.',
                ],
                'continueGame': True
            },
            {
                'messages': [
                    'I hope what you saw was worth it.',
                    'You lost 20 health and 25% resistance to the ring.'
                ],
                'continueGame': True,
                'increaseHealth': -20,
                'decreaseRingResistance': .75
            }
        )
    },
    {
        'event': '7. Boromir tries to take the ring',
        'preDecisionMessages': [
            'The ring\'s power is getting stronger with every step toward Mount Doom.',
            'It is so strong that Boromir has been consumed by it\'s power and tries to take the ring!' 
        ],
        'closeStepMessages': [
            'At the last moment, Aragorn saved you from Boromir!',
            'Boromir has been removed from your companions.'
        ],
        'decision': 'You are all alone when Boromir tries to take the ring. Do you draw your sword to fight him, or put the ring on and hide? (ring/sword) ',
        'decisions': (
            {
                'messages': [
                    'Good luck, Boromir is skilled with a sword!'
                ],
                'continueGame': True,
                'attack': {
                    'probability': 1.0,
                    'enemy': {
                        'name': 'Boromir',
                        'strength': 35
                    }
                },
                'companions': {
                    'remove': ['Boromir']
                }
            },
            {
                'messages': [
                    'Good luck, do not let the ring consume you!',
                ],
                'continueGame': True,
                'decreaseRingResistance': .75,
                'companions': {
                    'remove': ['Boromir']
                }
            }
        )
    },
    {
        'event': '8. You and Sam leave the Fellowship',
        'preDecisionMessages': [
            'In order to save the rest of the Fellowship from certain death, you decide to leave the group.',
            'You reluctantly allow Sam to come with you.',
            'Shortly after leaving the group, you and Sam meet a sly, mischevous character named Gollum.',
            'Gollum says he knows the way to Mordor and will show you how to get there. ' 
        ],
        'postDecisionMessages': [
            'You continue on with Gollum leading the way and Sam following close behind.'
        ],
        'decision': 'Do you trust Gollum is telling the truth? (y/n) ',
        'decisions': (
            {
                'messages': [
                    'Unfortunately, that choice was one of your last.',
                    'You attempt to make it through the Dead Marsh, but perished along the way.',
                    'Better luck next time!'
                ],
                'continueGame': False,
            },
            {
                'messages': [
                    'It is risky, but you do not know the way; you have no other choice.'
                ],
                'continueGame': True,
                'companions': {
                    'add': ['Gollum'],
                    'remove': ['Merry', 'Pippin', 'Aragorn', 'Legolas', 'Gimli', 'Gandalf']
                }
            }
        )
    },
    {
        'event': '9. Arrive at the Black Gate',
        'preDecisionMessages': [
            'You and Sam have arrived at the Black Gate of Mordor!',
            'It is heavily guarded, but it is the only way you know into Mordor.',
            'As you prepare to storm the gate, Gollum tells you he knows a secret way into Mordor.'
        ],
        'decision': 'Do you attempt to storm the Black Gate, or follow Gollum as he takes you the secret way? (gate/secret) ',
        'decisions': (
            {
                'messages': [
                    'Good choice - storming the Black Gate is certain death.',
                    'But beware, this close to Mordor danger lurks around every corner!'
                ],
                'continueGame': True,
                'attack': {
                    'probability': 1.0,
                    'enemy': {
                        'name': 'Shelob',
                        'strength': 20,
                    },
                    'responseOptions': {
                        'prompt': 'Oh no! Gollum has led you into Shelob\'s lair! Do you draw your sword and fight, or put on the ring to hide? (fight/hide) ',
                        'outcomes': (
                            {
                                'choice': 'fight',
                                'messages': ['Be careful, do not get caught in the web!']
                            },
                            {
                                'choice': 'hide',
                                'messages': [
                                    'Be quiet!'
                                ]
                            }
                        )
                    }
                }
            },
            {
                'messages': [
                    'Storming the Black Gate is risky, but it just might work!',
                    'Prepare for the fight of your life!',
                ],
                'continueGame': True,
                'attack': {
                    'probability': 1.0,
                    'enemy': {
                        'name': 'Orcs',
                        'strength': 50
                    }
                },
            }
        )
    },
    {
        'event': '10. You arrive at Mount Doom',
        'preDecisionMessages': [
            'You have made it all the way to Mount Doom!',
            'However, with every step closer, the ring\'s pull has become stronger.'
        ],
        'decision': 'Do you throw the ring into the fire to destroy in once and for all? Or do you keep it for yourself? (fire/keep) ',
        'decisions': (
            {
                'messages': [
                    'Middle Earth is yours to rule as you will!'
                ],
                'continueGame': True
            },
            {
                'messages': [
                    'Job well done! No one else in Middle Earth could have completed what you have.',
                    'Great job!'
                ],
                'continueGame': True
            }
        )
    }
]
