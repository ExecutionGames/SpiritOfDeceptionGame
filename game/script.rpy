# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hikari")
define mc = Character("[name]")
define v = Character("???", colour="#d183cb")
define r = Character("Ren")
define hn = Character("Hanako")
define t = Character("Teacher")
define d = Character("Dolos")

#FX Go here:
define flash = Fade(.25, 0.0, .75, color="#ffffff")


#BGs go here:
image futon_room = "images/bgs/pt1/Futon_Room.png"
image futon_room_night = "images/bgs/pt1/Futon_Room_Night.png"
image shrine_spring_cloudy = "images/bgs/pt3/Shrine_Spring_Cloudy.png"
image bedroom_day = "images/bgs/pt2/Bedroom_Day.png"
image bedroom_evening = "images/bgs/pt2/Bedroom_Evening.png"
image bedroom_night = "images/bgs/pt2/Bedroom_Night.png"
image bedroom_night_dark = "images/bgs/pt2/Bedroom_Night_Dark.png"
image street_spring_day = "images/bgs/pt2/Street_Spring_Day.png"
image street_spring_evening = "images/bgs/pt2/Street_Spring_Evening.png"
image street_spring_night = "images/bgs/pt2/Street_Spring_Night.png"
image street_spring_rain = "images/bgs/pt2/Street_Spring_Rain.png"
image city_morning = "images/bgs/pt2/City_Morning.png"
image city_afternoon = "images/bgs/pt2/City_Afternoon.png"
image city_night = "images/bgs/pt2/City_Night.png"
image city_raining = "images/bgs/pt2/City_Raining.png"
image outdoor_stairs = "images/bgs/pt1/Outdoor_Stairs.png"
image apartment_exterior = "images/bgs/pt1/Apartment_Exterior.png"
image apartment_exterior_night = "images/bgs/pt1/Apartment_Exterior_Night.png"
image livingroom_day = "images/bgs/pt2/Livingroom_Day.png"
image livingroom_night = "images/bgs/pt2/Livingroom_Night.png"
image livingroom_dark = "images/bgs/pt2/Livingroom_Dark.png"
image bathroom = "images/bgs/pt1/Bathroom.png"
image school_hallway = "images/bgs/pt2/School_Hallway_Day.png"
image classroom = "images/bgs/pt2/Classroom_Day.png"


#Kitsune Sprites Pt1:
image kitsune_neutral = "images/kitsune/kitsune-neutral.png" 
image kitsune_neutral_blush =  "images/kitsune/kitsune-neutral-blush.png"
image kitsune_smile = "images/kitsune/kitsune-smile.png"
image kitsune_smile_blush = "images/kitsune/kitsune-smile-blush.png"
image kitsune_upset = "images/kitsune/kitsune-upset.png"
image kitsune_upset_blush = "images/kitsune/kitsune-upset-blush.png"

#Hanako Sprites:
image hanako_uni_closed_frown = "images/hanako/hanako-uni-closed-frown.png"
image hanako_uni_closed_frown_blush = "images/hanako/hanako-uni-closed-frown-blush.png"
image hanako_uni_closed_open = "images/hanako/hanako-uni-closed-open.png"
image hanako_uni_closed_open_blush ="images/hanako/hanako-uni-closed-open-blush.png"
image hanako_uni_closed_smile = "images/hanako/hanako-uni-closed-smile.png"
image hanako_uni_closed_smile_blush = "images/hanako/hanako-uni-closed-smile-blush.png"
image hanako_uni_frown = "images/hanako/hanako-uni-frown.png"
image hanako_uni_frown_blush = "images/hanako/hanako-uni-frown-blush.png"
image hanako_uni_open = "images/hanako/hanako-uni-open.png"
image hanako_uni_open_blush = "images/hanako/hanako-uni-open-blush.png"
image hanako_uni_smile = "images/hanako/hanako-uni-smile.png"
image hanako_uni_smile_blush = "images/hanako/hanako-uni-smile-blush.png"

#Ren Casual Sprites:
image ren_casual_frown = "images/ren/casual/ren-casual-frown.png"
image ren_casual_frown_blush = "images/ren/casual/ren-casual-frown-blush.png"
image ren_casual_open = "images/ren/casual/ren-casual-open.png"
image ren_casual_open_blush = "images/ren/casual/ren-casual-open-blush.png"
image ren_casual_smile = "images/ren/casual/ren-casual-smile.png"
image ren_casual_smile_blush = "images/ren/casual/ren-casual-smile-blush.png"

#Hikari Casual Sprites:
image hikari_casual_frown = "images/hikari/hikari-casual-frown.png"
image hikari_casual_frown_blush = "images/hikari/hikari-casual-frown-blush.png"
image hikari_casual_open = "images/hikari/hikari-casual-open.png"
image hikari_casual_open_blush = "images/hikari/hikari-casual-open-blush.png"
image hikari_casual_smile = "images/hikari/hikari-casual-smile.png"
image hikari_casual_smile_blush = "images/hikari/hikari-casual-smile-blush.png"

#Hikari School (Summer) Sprites:
image hikari_uni_frown = "images/hikari/Uniform/hikari-uni-frown.png"
image hikari_uni_frown_blush = "images/hikari/Uniform/hikari-uni-frown-blush.png"
image hikari_uni_open = "images/hikari/Uniform/hikari-uni-open.png"
image hikari_uni_open_blush = "images/hikari/Uniform/hikari-uni-open-blush.png"
image hikari_uni_smile = "images/hikari/Uniform/hikari-uni-smile.png"
image hikari_uni_smile_blush = "images/hikari/Uniform/hikari-uni-smile-blush.png"


#Misc. Images and Video:
image mm = "gui/main_menu.png"
image space = Movie(play="images/bgs/space.webm")
image trippy = Movie(play="images/bgs/trippy.webm")

image splash = "splash.png"

transform halfleft:
    xalign 0.25
    yalign 1.0
    
transform halfright:
    xalign 0.75
    yalign 1.0




# The game starts here.

label splashscreen:
    scene black

    show mm with dissolve

    "The version of the game you are about to play is in Pre-Alpha stages, therefore, some aspects of it are subject to change"

    "This game is not reccommended to those who suffer from anxiety or depression as it depicts disturbing images that may cause some viewers to feel uncomfortable"
        
    #this should be a break here but it is a bug and cannot be fixed
        
    "By pressing 'Agree' you agree to viewing very disturbing content and horror elements"


    menu:

        "By pressing 'Agree' you agree to viewing very disturbing content and horror elements"

        "Agree":
            jump splash

        "Disagree":
            $ renpy.quit()

    return


label splash:
    play music "main-menu-theme.ogg" fadeout 1
    scene black
    with Pause(1)
    
    scene splash with dissolve 
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)
    
    show text "{color=#ffffff}This game is not for those who are easily disturbed...{/color}" 
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    
    return 


label start:

    call variables

    $ name = renpy.input("What is your name?")
    $ name = name.strip()

    scene black with dissolve
    with Pause(1)

    scene black with dissolve
    with Pause(1)

    scene black
    play music "bgan1.ogg" fadeout(1)

    "An unexplainable and aching feeling echoes through your head and body."

    "You feel like you have been stuck in this void forever..."

    "Is this... how it always has been?"

    "What was it that brought your mind to this hellish state...?"

    "You try to open your eyes, however... there is absolutely nothing around you."

    "Nothing but the void of space, the collapse of what appears to be worlds fills your hearing."

    "It all feels cold..."

    mc "This is all just a bad dream..."

    mc "I must wake up from this..."

    show space with dissolve

    v "{b}There is nowhere to run [name]...{/b}"

    mc "Who are you..?"

    mc "And more importantly... {i}WHAT{/i} are you?"

    v "{b}I do not owe you an explaination...{/b}"

    v "{b}You should already know who I am by now...{/b}"

    v "{b}Have you forgotten what led you here?{/b}"

    v "{b}Perhaps a little reminder wouldn't hurt...{/b}"

    v "{b}Here... let me show you...{/b}"

    scene black with dissolve

    scene futon_room with dissolve
    play music "bgm3.ogg"

    "What the hell happened?"

    "I had yet another weird dream..."

    "It doesn't help that I have a pounding headache..."

    v "Hellooooo?"

    v "Anybody in there??"

    show hikari_casual_smile with easeinright

    v "Hey, there you are!"

    "It seems that today I get to hang out with my sister."

    "Normally, it would be fine, but I have a pounding headache right now..."

    "I haven't really been able to spend much time with her ever since we started High School..."

    "We study in different schools."

    "If I remember correctly, she is studying in a All-Girls School just down the block."

    "She also doesn't come over to her own house very often and stays over at other people's houses"

    "But alas... She is still my sister, regardless of how confusing and sometimes annoying she can get."

    mc "Hey, Hikari. Nice seeing you."

    h "Hey, [name]! How are you doin'?"

    mc "I'm good, I'm good. You?"

    h "Well... I've been doing alright. Say... do you have time?"

    mc "I suppose so... What's up?"

    h "Well... I was wondering if you would like to join me! I'm going to the shrine!"

    mc "The shrine? Why there out of all the places? It's not time yet."

    h "Well, that's true but..."

    show hikari_casual_open 

    h "I was wondering if you would be willing to help with something there?"

    mc "If you are planning on dragging me into some weird occult stuff, please count me out of it..."

    mc "We already have enough trouble as is..."

    "Ever since she started staying over at one of her friends' house she started getting interested in the occult."

    "I never really had any interest in  it, as it seemed like something that doesn't really sound plausable in our  world."

    "I mean, come on... Spirits? Ghosts? Voodoo? Doesn't hold much ground."

    mc "No way, Hikari. I'm not joining into whatever ritual you guys are going to do."

    h "It's not going to be a ritual, dummy! Come on, when have I ever let you down? You can trust me!"

    "I can remember at least a couple of times where we had to make a run for it because of her shenanigans."

    "But foolish me keeps trusting her."

    "Hope dies last, as they say."

    mc "I really don't want more trouble."

    mc "Besides, don't you remember what happened last time we went somewhere with your friends?"

    show hikari_casual_frown

    h "That--"

    h "That was an incident..."

    h "Ahahahahah...~"

    "Hikari and her friends almost got arrested because they thought it'd be cool to light cookies on fire and throw them at people's faces."

    "They almost burned down the entire park after dropping one of them on the grass."

    mc "I don't know how getting detained due to suspected arson was an accident, but you do you."

    h "Please come join us... I promise it'll be worth it this time!"

    "I dejectedly agree to Hikari's request."

    mc "Fine... just don't burn down the shrine... I don't wanna have to explain everything to the cops {i}AND{/i} our parents again!"

    hide hikari_casual_frown
    show hikari_casual_smile

    h "Yes! Sweet! Come on!"

    scene black with dissolve

    scene shrine_spring_cloudy with dissolve

    show ren_casual_frown at halfleft with easeinleft
    show hikari_casual_frown at halfright with easeinright

    v "I'm telling you Hikari, this will change everything!"

    h "I never doubted you. I'm sure it will all be fine. Did you buy everything like instructed?"

    v "Yeah. I even got some extras just in case we lose them."

    h "Awesome! Oh, [name], you haven't met Ren, have you?"

    r "Nice to meet you [name]. I'm Ren."

    mc "Oh uh... Hi Ren."

    r "Is [name] also going to participate?"

    h "Yes. Because he is my older brother!"

    mc "Hikari!"

    h "Sorry, sorry."

    hide hikari_casual_frown
    show hikari_casual_open at halfright

    h "Anyways, let's start!"

    scene black with dissolve
    show shrine_spring_cloudy with dissolve

    stop music fadeout(5)

    "Hikari and Ren start lighting a bunch of candles and chanting a phrase over and over"

    "You try to listen in but the phrase is too incoherent to interpret"

    show ren_casual_smile at halfleft
    show hikari_casual_smile at halfright

    mc "Uhm... what are you guys doing?"

    r "Relax, [name]. Me and Hikari got everything under control."

    mc "If you guys are trying to summon something it's not really gonna happen, you know?"

    r "Don't worry, everything will be fine!"

    h "Yeah, trust me, okay?"

    scene black with dissolve
    show shrine_spring_cloudy with dissolve
    play music "bgm3.ogg" fadein(1)

    "After what seems to be an hour they kept chanting and waving sticks of insense"

    show hikari_casual_frown at halfright
    show ren_casual_frown at halfleft

    h "Man... nothing happened. We wasted 20 bucks just for this to fail..."

    r "I thought you had it all figured out..."

    mc "Didn't I tell you guys? None of this voodoo stuff or whatever you are doing is real."

    mc "I remember telling you not to believe everything on the internet, Hikari..."

    h "But this one was very plausable! It looked real and had people do it! They had amazing luck afterwards."

    h "I needed that luck to get a better score on my tests..."

    mc "Did you seriously go all this way just to guarantee you some luck on your exams? Your time would've been better spent studying instead!"

    h "Now that's just mean!"

    r "You guys, don't worry. It could've worked? We can't exactly measure luck, can we?"

    r "Besides, didn't you say it takes a while for the luck to come to you?"

    h "I guess so, but..."

    mc "Ren, Hikari, I don't know where you guys read this stuff on but I'm out of here." 
    
    mc "If you want to keep trying, then you are more than welcome to do so."

    mc "And Hikari, please go and study for your tests instead..."

    scene black with dissolve

    "You leave Hikari and Ren at the shrine and start walking back to your house."

    scene black with dissolve
    play music "bgm4.ogg" fadein(1)

    scene street_spring_rain with dissolve

    "As you walk through to your house, it suddenly starts raining."

    "It's a shame that on days like these you didn't really bring an umbrella."

    "Fortunately, you live close by to the shrine."
    
    "As you cross the street you bump into a girl that you have never really seen before."

    show hanako_uni_frown_blush with hpunch

    v "S-Sorry..."

    v "I didn't really mean to do that..."

    mc "Ah, no problem. Sorry as well."

    hide hanako_uni_frown_blush with easeoutleft

    "She runs past you and by the time you turn to ask her for her name, she is already far gone."

    "You start to walk back to your house again."

    scene outdoor_stairs with dissolve

    "You finally reach the stairs to your house."

    "Suddenly, you hear the voice of a familiar girl"

    h "Heeeeeeeyyy! Wait up!"

    show hikari_casual_frown_blush with easeinright

    "Breathless from running, she finally musters enough energy to speak to you after seemingly running a marathon."

    h "I caught up to you right on time!"

    h "The things..."

    h "*pant*"

    h "The thing we did at the shrine—"

    h "*pant*"

    mc "Just catch your breath first and then talk! Dummy..."

    "She takes a few moments to catch her breath and then starts to speak again"

    hide hikari_casual_frown_blush
    show hikari_casual_open

    h "The thing we did at the shrine worked! It took a bunch of attempts but it finally did!"

    mc "And how exactly did you find out it did..?"

    h "I found this!"

    "She shows you a 5 dollar bill that has been crumpled up and there seems to be stains of soda on the bill."

    mc "Hikari..?"

    h "Yeah?"

    mc "That's just ordinary luck, stupid."

    h "Huh?? What do you mean??"

    mc "Anybody can find a scrumpled five dollars laying around!"

    mc "Besides, as I have told you multiple times before and I'll say it again..."

    mc "Spirits."

    mc "Do not."

    mc "Exist!"

    hide hikari_casual_open
    show hikari_casual_frown

    h "But... I felt something change! I knew it worked after a while..."

    mc "I honestly won't believe you until there is tangible proof that it worked."

    mc "And five dollars that fell out of someone's pocket after being scrumped up like that is just ordinary luck."

    h "Man... you're such a drag. No wonder why you have no friends."

    mc "Wha—"

    mc "Where did {b}{i}that{/b}{/i} come from??"

    h "Well you were the mean one first!"

    mc "Okay, I'm sorry! Jeez..."

    h "Hmph!"

    mc "Okay, how about I let you stay over at my house? It's raining and I don't want you to catch a cold. Our parents will kill me if I let you get sick."

    h "Not unless you buy me ice cream first!"

    "You let out a long sigh"

    mc "Okay, we have a deal. I'll get you some ice cream."

    h "And for the record... I'm still mad at you! You won't buy your way out of this one!"

    mc "Okay, got it."

    hide hikari_casual_frown with easeoutleft

    "You and Hikari start walking up to your apartment"

    scene black with dissolve
    stop music fadeout(1)

    scene apartment_exterior with dissolve
    play sound "unlock.ogg" noloop
    play music "bgm4.ogg"

    "You slowly unlock the door and start to open it"

    play sound "rain.ogg" fadeout(1) loop

    "The rain is much more audible as it starts to turn into a storm"

    "You quickly get into your apartment."

    scene black with dissolve
    stop music fadeout(1)
    stop sound fadeout(1)

    scene livingroom_night with dissolve
    play sound "room_ambience.ogg" loop

    "You are finally home and can sit down."

    "Hikari quickly sprawls all over the couch and you are left sitting on the floor"

    show hikari_casual_smile with easeinbottom

    h "Ahhh, there is no place like at big brother's house!"

    mc "Yeah, yeah. Honestly, I agree. This place is pretty comfortable."

    h "I'm also very happy that you will be buying me ice cream! Hehehe~"

    mc "Yeah, that too. I'm gonna buy myself some too, honestly."

    h "Yeah, you're probably gonna get vanilla again. Typical."

    mc "Hey! What's that supposed to mean??"

    h "Ahahaha, nothing, nothing. Don't worry about it!"

    mc "Mmmh..."

    h "There, there."

    hide hikari_casual_smile 
    show hikari_casual_open 

    h "Honestly, [name]... I'm surprised."

    mc "Hm? What do you mean?"

    h "Well..."

    h "I'm surprised you don't believe in spirits and such."

    h "It's honestly pretty fascinating stuff and it does tend to explain some of the unsolved mysteries of everything around us."

    h "Like how sometimes when you wish for something really, really hard it comes true!"

    h "That can't be mere coincidence, right?"

    mc "I suppose you have a point there, however... I've never really seen anything spiritual to begin with."

    mc "So I'm mostly skeptical of the concept because it is not really based on facts and is based on some... random fairy tales."

    hide hikari_casual_open
    show hikari_casual_frown

    h "Well... they aren't really 'Fairy tales' because there is a lot more to the spiritual realm than what meets the eye!"

    mc "How do you know so much about this stuff anyway?"

    h "Well, remember my friend from school?"

    mc "The one we just met? Ren?"

    h "No, no, not him. Hanako."

    h "Also, I study at an All-Girls school, remember?"

    mc "Ah, yeah. Sorry about that"

    h "No problem."

    mc "But like... Hana-who-now?"

    h "Hanako? You've never met her?"

    mc "Not even once in my life."

    h "You two really should meet!"

    h "Anyways... Well she was the one who made me curious about this kind of stuff."

    h "She always been kind of a nerd and a bookworm. She did give off some unsettling vibes at first but we started to talk a bit and she turned out a really nice person!"

    h "Basically, what I'm saying is... she taught me the basics of this spirit realm thing."

    mc "I see..."

    "Who would've known that someone in Hikari's own school would be the one to influence her to that degree."

    "I wonder, though... did the whole 'ritual' really work? Is she really as lucky as she says?"

    "Meh... No point in asking that now, really."

    "Without realizing it, you have spent a few hours talking and it turned night time"

    h "Now, I don't wanna sound naggy but.."

    mc "Hm?"

    h "I was promised ice cream!"

    mc "Ah, yeah, sorry. I'll go get it now."

    h "Okay! Thank you!~"

    mc "I will have to go to the store real quick, do you mind staying alone for a bit?"

    h "Alright, I'll stay and wait for you."

    h "Make sure to stay safe!"

    "Unfortunately, due to the fact that it's night time, most stores aren't open anymore."

    "Man... I really should have gotten to the store earlier. Now I have to go to the city to get her ice cream..."

    "You start to put on your clothing and put a raincoat on with rainboots just in case."

    "You check your pockets."

    "Keys, wallet, phone... Everything is in place."

    play sound "door_close.ogg" noloop

    scene black with dissolve

    "You venture out to the city..."

    scene city_night with dissolve
    play sound "rain.ogg" loop

    "As you walk through the city, everything is wet and reflective."

    "Cars almost splash you as they pass you by"

    "I really should've gotten to the store earlier..."

    play music "bgm5.ogg"
    play sound "wet_run.ogg" noloop

    mc "What the hell was that??"

    play sound "rain.ogg" loop

    mc "Who's there??"

    "There was no answer..."

    mc "You really shouldn't scare people like that whoever you are!"

    "Whoever that ran past you does not answer."

    mc "Damn it... I should get out of here. Let's just get this stupid ice cream and get the hell out of here."

    scene black with dissolve

    "You walk to the store to grab the ice cream you promised to Hikari and you return back home."

    scene apartment_exterior_night with dissolve
    play sound "unlock.ogg" noloop

    "You fumble with the doorknob and unlock the door"

    scene livingroom_night with dissolve
    play sound "room_ambience.ogg" loop

    "A sense of safety fills your whole being."

    "Finally... I'm home. I don't have to worry anymore."

    "You lock the door behind you, hoping that whatever it was that you saw in the city will not go through it."

    show hikari_casual_frown with easeinright

    h "Big brother? Are you okay?"

    mc "Y-Yeah... I'm okay."

    h "You look kinda pale. Did something happen?"

    mc "No, don't worry about it. I'm fine, see?"

    "You show Hikari a big smile."

    h "Okay, whatever you say..."

    h "Did you get my ice cream?"

    mc "Ah, yeah. Here you go."

    "You give Hikari the ice cream you bought from the store."

    hide hikari_casual_frown
    show hikari_casual_smile

    h "Yay!~"

    mc "I'm gonna go and lay down for a bit..."

    hide hikari_casual_smile
    show hikari_casual_frown

    h "Hm? Okay."

    "You feel a pit in your stomach..."

    scene bedroom_night with dissolve

    "You lay down in your bed."

    mc "What was that just now? It most likely was someone running to get to shelter because of the rain!"

    mc "Yeah, I'm sure it was that!"

    mc "I don't feel well..."

    mc "I think I will rest my eyes for a bit..."

    scene black with dissolve

    "Closing your eyes, you hear only the sound of the rain and the ongoing traffic outside your room."

    "As you keep your eyes closed..."

    stop music fadeout(5)

    "You start to fall asleep..."

    "Your body doesn't feel like your own anymore."

    stop sound fadeout(5)

    "Something feels..."

    "...not right..."

    scene black with dissolve

    "..."

    "..."

    "..."


    scene bedroom_night_dark with dissolve
    play sound "phone.ogg" loop

    "You suddenly hear your phone buzzing..."

    "..."

    menu:
        "Pick up.":
            $ good_choices += 1
            call pick_up
        "Ignore it.":
            $ bad_choices += 1
            pass

    stop sound

    mc "I can't feel my body..."

    "You suddenly feel the urge to vomit again."

    scene bathroom with dissolve

    "You rush towards the bathroom, stumbling around the couch and objects around your apartment."

    "You vomit the contents of your stomach into the toilet bowl."

    mc "What the hell is happening to me..?"

    mc "What could cause something like this??"

    "You look at yourself in the mirror after flushing the toilet."

    "Your face is paler than snow."

    play sound "fall.ogg" noloop

    "You suddenly collapse on the floor."

    "You slowly lose consciousness..."

    scene black with dissolve

    "What is... happening to me...?"

    "I can't..."

    "Feel..."

    stop music fadeout(10)

    "My body..."

    "..."

    scene bedroom_day with dissolve
    play music "bgm1.ogg" fadein(5)

    mc "Ugh..."

    "You wake up on your bed somehow."

    mc "What happened..?"

    show hikari_casual_frown with easeinright

    h "[name]..?"

    h "[name]... please wake up..."

    h "[name]! Oh thank god!"

    mc "Hikari..? What the hell happened..?"

    h "I should be asking YOU that! Why were you passed out on the floor?"

    mc "Huh?"

    "I was passed out on the floor..?"

    if good_choices == 1:
        call rememberance
    else:
        pass

    "I don't remember anything else..."

    "My mind is so hazy..."

    h "You were passed out on the floor and you had your phone in your hand."

    h "What were you doing?"

    mc "I... I don't remember anything."

    h "Are you sure you didn't hit your head or something?"

    mc "I mean... I could have? I don't know."

    h "Man... You really need to be more careful!"

    h "Mom called earlier, she asked me to check up on you."

    mc "Wait, did you tell her what happened?"

    h "Yeah, and she got super worried about you!"

    mc "I can understand that..."

    "Man... my head is pounding..."

    mc "Do you think you can give me some medecine?"

    h "Sure. Hold right there."

    hide hikari_casual_frown with easeoutright

    "Hikari leaves to the meds cupboard to grab some aspirin."

    "Though, would it really help?"

    show hikari_casual_frown with easeinright

    h "Here you go."

    "She drops in a pill of aspirin in a glass cup."

    "You start to chug it down."

    h "Now... I don't know if you will be able to go to school in this shape."

    mc "I... I think I'll be fine. I should go once my headache subsides, though."

    h "Alright, I'll be here and then escort you to the gate of your school."

    mc "Thanks, Hikari... I'm sorry I worried you..."

    hide hikari_casual_frown
    show hikari_casual_smile

    h "It's alright. You're my big brother! We look after each other, remember?"

    mc "Yeah... Thank you."

    "I fail to sound nearly as enthusiastic as Hikari."

    h "I'll go change and then we can walk to your school."

    "I nod and agree."

    hide hikari_casual_smile with easeoutright

    "And so it begins..."

    "A brand new day..."

    scene black with dissolve
    stop music fadeout(5)

    jump day_1

    # This ends the game.

    return

label day_1:

    scene school_hallway with dissolve
    play music "bgm4.ogg"
    show hikari_uni_frown with easeinright

    h "We are here now, [name]."

    mc "Thanks..."

    h "Are you sure you can take care of yourself from here on out?"

    mc "Yeah, I should be alright."

    h "Okay, then. I'll come pick you up later, okay?"

    mc "Yeah, sure. Thank you, Hikari."

    h "No worries."

    hide hikari_uni_frown with easeoutright

    "Yesterday..."

    stop music fadeout(3)
    call flashback

    scene school_hallway with dissolve
    play music "bgm4.ogg"

    "It felt..."

    "Unreal..."

    "I don't know what happened but it was not ordinary."

    "In any case..."

    "I should worry about getting to class."

    scene classroom with dissolve

    "The school day is as ordinary as ever. Nothing out of the usual"

    "While the school day goes on your head is still pounding"

    t "Now who can tell me what the author had in mind when writing the story?"

    t "Anyone?"

    v "They probably meant that their lover is roaming the earth as a ghost?"

    t "Not quite."

    t "On the surface it does sound like that but..."

    scene black with dissolve

    "Class continues as normal."

    "You feel your eyes get heavier."

    scene trippy with dissolve
    play music "bgan1.ogg" fadein(5)

    v "{b}{font=hackattack.otf}Can you comprehend the situation you are in?"

    mc "What do you mean..? What even are you??"

    v "{b}{font=hackattack.otf}I am Dolos. I am god here."

    d "{b}{font=hackattack.otf}You should already know who I am..."

    mc "I..."

    d "{b}{font=hackattack.otf}Silence..."

    d "{b}{font=hackattack.otf}[name]... I come to you with a purpose..."

    d "{b}{font=hackattack.otf}Are you willing to listen?"

    menu:
        "Listen":
            $ good_choices += 1
            call listentoplan
        "Refuse":
            $ bad_choices += 1
            pass
    

    scene black with dissolve

    "You feel your mind get clearer and suddenly wake up..."

    return
    
label flashback:

    scene bathroom with flash

    "*vomiting*"

    v "{b}{font=hackattack.otf}HGJFyteTYRFDr647TYGVyte6GDBjabd654S4DyasvdgHASGD65qweVKjdff8y6DJHGwed{/b}{/font}"

    mc "What..?"

    mc "I don't understand..."

    v "{b}{i}{font=hackattack.otf}YTR78gbh8Y53908HFgfkgjhfTREH;{/b}{/i}{/font}"

    scene black with dissolve
    play sound "fall.ogg" noloop
    pause(2)

    return

label pick_up:

        stop sound 
        play music "bgm5.ogg" fadein(5)

        "You decide to pick up the phone..."

        v "Hello?"

        mc "Who is this?"

        v "Do you know where I can find {font=hackattack.otf}{b}{i}GhvkhARY3556gftrrHAHGT{/i}{/b}{/font}?"

        mc "Who..?"

        v "N-Nevermind..."

        play sound "hang_up.ogg" noloop

        "The voice over the phone felt so cold..."

        mc "Who the fuck was that?"

        return

label rememberance:
        
    "All I remember was that... voice from yesterday..."
    
    return

label variables:

    define good_choices = 0
    define bad_choices = 0

    $ good_choices = 0
    $ bad_choices = 0

    return

label imports:

    init python:

        import os
        pcName = os.getenv('username')

    return

label listentoplan:

    "You decide to listen in on Dolos' plan"

    d "{b}{font=hackattack.otf}I will not touch this world if only you accept to destroy an entity..."

    mc "What?"

    d "{b}{font=hackattack.otf}An entity of great importance should come to you in three days."

    d "{b}{font=hackattack.otf}You must destroy them."

    d "{b}{font=hackattack.otf}If you do so, I will reward you greatly."

    d "{b}{font=hackattack.otf}Great fortune and romance will come your way, must you do as I say."

    d "{b}{font=hackattack.otf}If you refuse... misfortune will befall on your loved ones."

    d "{b}{font=hackattack.otf}You wouldn't want that to happen, do you, [pcName]?"

    mc "Who... who is [pcName]..?"

    d "{b}{font=hackattack.otf}I believe you should know that better than anyone..."

    d "{b}{font=hackattack.otf}Consider my offer [name]."

    return