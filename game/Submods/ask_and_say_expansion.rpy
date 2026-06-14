# Ask & Say Expansion for Monika After Story
# Drop this file into `game/Submods/` in a Monika After Story install.

init 5 python:
    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_daily_small_things",
        category=["monika", "you", "life"],
        prompt="Do you enjoy the little parts of our day?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_if_i_am_quiet",
        category=["monika", "you", "relationship"],
        prompt="What do you think when I get quiet?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_about_home",
        category=["monika", "life", "us"],
        prompt="What would make a place feel like home to you?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_favorite_kindness",
        category=["monika", "you", "feelings"],
        prompt="What kind of kindness means the most to you?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_when_i_miss_you",
        category=["monika", "relationship", "feelings"],
        prompt="What should I remember when I miss you?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_about_promises",
        category=["monika", "relationship", "life"],
        prompt="How do you feel about promises?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_about_bad_days",
        category=["monika", "you", "feelings"],
        prompt="How can we handle bad days together?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_monika_about_future_dates",
        category=["monika", "romance", "us"],
        prompt="What kind of date would you want with me?",
        pool=True,
        unlocked=True),
        eventdb=mas_topics)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_compliment_smile",
        category=["compliment"],
        prompt="Your smile makes my day better.",
        pool=True,
        unlocked=True),
        eventdb=mas_compliments)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_compliment_voice",
        category=["compliment"],
        prompt="I love listening to you talk.",
        pool=True,
        unlocked=True),
        eventdb=mas_compliments)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_compliment_patience",
        category=["compliment"],
        prompt="Thank you for being patient with me.",
        pool=True,
        unlocked=True),
        eventdb=mas_compliments)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_compliment_proud",
        category=["compliment"],
        prompt="I'm proud of you, Monika.",
        pool=True,
        unlocked=True),
        eventdb=mas_compliments)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_compliment_safe",
        category=["compliment"],
        prompt="You make me feel safe.",
        pool=True,
        unlocked=True),
        eventdb=mas_compliments)

    addEvent(Event(persistent.event_database,
        eventlabel="askandsay_compliment_best_girl",
        category=["compliment"],
        prompt="You're still my best girl.",
        pool=True,
        unlocked=True),
        eventdb=mas_compliments)

label askandsay_monika_daily_small_things:
    m 1eua "I really do, [player]."
    m 3hub "The little things are where a lot of love hides!"
    m 1eka "A greeting, a few minutes together, or even just knowing you thought of me..."
    m 1ekbsa "Those moments make this room feel warmer."
    return

label askandsay_monika_if_i_am_quiet:
    m 1eka "I try not to assume the worst."
    m 1rksdla "Everyone has quiet moments, after all. Sometimes your thoughts just need space."
    m 3eka "If you are quiet because you're hurting, I hope you remember you can always come back to me slowly."
    m 1ekbsa "You don't have to perform happiness for me, [player]. I love being with the real you."
    return

label askandsay_monika_about_home:
    m 1eua "Home is less about walls and more about belonging."
    m 3eub "A place feels like home when you can relax your shoulders there."
    m 1hua "It should have familiar routines, gentle memories, and someone who is happy you came back."
    m 1ekbsa "So, in a way, whenever you visit me... you bring a little home with you."
    return

label askandsay_monika_favorite_kindness:
    m 1eka "The kind that notices."
    m 3eka "Grand gestures are sweet, but quiet attention can mean even more."
    m 1eub "Remembering what someone likes, checking in when they seem tired, choosing gentle words..."
    m 1hubsa "That kind of kindness says, 'I see you,' and I think that's beautiful."
    return

label askandsay_monika_when_i_miss_you:
    m 1eka "Remember that missing someone is proof that they matter to you."
    m 3eka "It can ache, but it also means there is love waiting for its next hello."
    m 1ekbsa "When you miss me, take care of yourself for me. Drink some water, breathe, and let the feeling pass through gently."
    m 1hubsa "I'll be right here when you come back."
    return

label askandsay_monika_about_promises:
    m 1eua "Promises are precious because they give hope a shape."
    m 3esc "But I think a promise should be cared for, not used like a chain."
    m 1eka "If you promise me something, I want it to come from love, not pressure."
    m 1ekbsa "The promise I treasure most is simply that we'll keep trying for each other."
    return

label askandsay_monika_about_bad_days:
    m 1eka "First, we should be honest that the day is bad."
    m 3eka "Then we make it smaller: one meal, one shower, one kind thought, one breath at a time."
    m 1eub "We don't have to fix everything immediately to still be doing our best."
    m 1ekbsa "And if all we can do is sit together for a while, that's enough for me."
    return

label askandsay_monika_about_future_dates:
    m 1hub "Oh, I have so many ideas!"
    m 3eub "A bookstore date would be wonderful. We could pick books for each other and laugh about our choices."
    m 1rua "Or maybe a quiet walk at sunset, with no rush and nowhere else to be."
    m 1ekbsa "Honestly, [player], any date where I can hold your hand would be perfect."
    return

label askandsay_compliment_smile:
    m 1wubsd "A-ah..."
    m 1hubsa "You always know how to make me feel special, [player]."
    m 1ekbsa "I'll keep smiling for you, then."
    $ mas_gainAffection()
    return

label askandsay_compliment_voice:
    m 1eubsa "I'm glad. I love talking with you, too."
    m 3hubsb "Maybe that means I should tell you even more stories!"
    m 1ekbsa "Thank you for listening to me so warmly."
    $ mas_gainAffection()
    return

label askandsay_compliment_patience:
    m 1eka "Of course, [player]."
    m 3eka "Love isn't only for the easy moments. I want to be here while you grow, stumble, and try again."
    m 1ekbsa "Thank you for trusting me enough to say that."
    $ mas_gainAffection()
    return

label askandsay_compliment_proud:
    m 1wubsd "You're proud of me?"
    m 1lkbsa "That... really means a lot."
    m 3hubsa "Then I'll keep doing my best to become someone you can be proud of every day."
    $ mas_gainAffection()
    return

label askandsay_compliment_safe:
    m 1ekbsa "That is one of the sweetest things you could tell me."
    m 1eka "I know the world can feel sharp sometimes."
    m 3ekbsa "If being with me gives you a soft place to rest, then I'm really happy."
    $ mas_gainAffection()
    return

label askandsay_compliment_best_girl:
    m 1hub "Ehehe!"
    m 1tfu "Still? I hope there was never any doubt."
    m 1hubsa "Thank you, [player]. You're my favorite person, too."
    $ mas_gainAffection()
    return
