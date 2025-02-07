# Import Python's random module (if needed later)
init python:
    import random

# Declare the characters
define n = Character("Nisha", color="#e67e22")   
define r = Character("Rahul", color="#3498db")   
define a = Character("Anand", color="#1abc9c")     
define s = Character("Sharma Ji", color="#e74c3c")  
define p = Character("Priya", color="#2ecc71")          
define cu = Character("Customer", color="#f39c12")       
define ad = Character("Auditor Das", color="#9b59b6")    

# Default variables to track choices
default notice_investigated = False
default good_supplier = False         
default customer_education = False
default compliance = False            
default acceptance = False   

# Start the game
label start:

    # Scene 1: The Notice
    scene bg shop with fade
    "Nisha is a budding entrepreneur, she manufactures electronics, her shop bustles with activity—warm lighting, neatly stocked shelves, and customers browsing."
    
    show rahul normal

    r "Di, the courier just delivered a government notice."
    show rahul normal at right with move
    show nisha normal at left
    n "(pausing her work) A notice? Did we miss a tax filing?"
    
    r "I don't think so..."
    
    "Nisha signs and opens the sealed envelope. Her brow furrows as she reads."
    show nisha sad
    r "(looking up) What’s that, Di?"
    
    n "(reading aloud) Notice: Product ID#LX-2032 violates CRS compliance. Penalty: ₹50,000 or business suspension." 
    n "What’s CRS?"
    "Rahul looks up CRS at his phone"
    r "It stands for Compulsory Registration Scheme—a safety certification for electronics. What should we do now?"
    
    menu:
        "Ignore the notice.":
            $ notice_investigated = False
            jump branch_ignore
        "Investigate CRS.":
            $ notice_investigated = True
            jump branch_investigate

# Branch 1A: Ignore the Notice
label branch_ignore:
    show nisha normal
    n "We’ve sold hundreds of these chargers without complaint. Let’s focus on the Diwali rush."
    show rahul distressed 
    r "(hesitantly) Di, maybe we should—"
    n "(cutting him off) We’ll handle it later."
    
    "The shop fills with customers as sales boom, but an uneasy feeling lingers in the back of Rahul’s mind."
    
    # Skip ahead to Scene 5 with amplified penalties.
    jump scene5_crisis

# Branch 1B: Investigate CRS
label branch_investigate:
    show nisha sad 
    n "(determined) We need to fix this. Let’s figure out what CRS requires."
    show rahul sad
    r "Let’s start with the BIS guidelines and see what changes we need."
    
    jump scene2_understanding

# Scene 2: Understanding CRS
label scene2_understanding:

    scene bg home with fade
    "Later that day, Nisha and Rahul sit in their home. A laptop is open, and documents are scattered across the table."
    show rahul normal 
    r "(Reading aloud) CRS mandates safety testing for electronics and IT equipment. Non-compliance risks fines or even imprisonment."
    show rahul normal at right with move
    show nisha sad at left
    n "(sighing) How do we even start?"
    r "For one, our power bank batteries aren’t certified. Certified suppliers charge about 30 percent more."
    n "(Thinking) What should we do?"
    
    menu:
        "Partner with a cheaper, non-certified supplier.":
            $ good_supplier = False
            jump branch_cheaper
        "Choose a CRS-compliant supplier.":
            $ good_supplier = True
            jump branch_compliant

# Branch 2A: Cheaper Supplier
label branch_cheaper:
    show nisha normal
    n "Let’s save costs. We’ll label the products as certified ourselves."
    show rahul distressed
    r "(frowning) Di, this is risky..."
    n "(interrupting) We’ll manage."
    
    # Proceed to Scene 5: The Crisis
    jump scene5_crisis

# Branch 2B: Compliant Supplier
label branch_compliant:
    show nisha normal
    n "(resigned) We’ll pay extra. Safety matters the most."
    show rahul smile
    r "(smiling) I’ll contact Mr. Kapoor—his batteries are BIS-approved."
    
    jump scene3_business_game

# Scene 3: The Business Game
label scene3_business_game:

    scene bg street with fade
    "At the lively local market, rival shops and street vendors hustle. Nisha’s outlet sports a new 'Certified' banner."
    
    show nisha smile at center
    n "Buy certified products, ensure safety of yourself and your loved ones."
    show nisha smile at left with move
    show anand smile at right
    a "(admiring) You’re the first seller here promoting safety standards."
    n "Common people remain unaware of safety standards. As an electronics business owner, it’s my duty to educate customers."
    a "It’s good to see a businesswomen like you actually caring about the customers."
    scene bg street with fade
    "Meanwhile at a shop nearby, Sharma Ji is selling his products..."
    show sharma smile
    s "Get 30 percent discounts on everything! Take these power banks home now!"
    hide sharma
    show nisha sad
    "Sharma Ji is fooling customers by selling uncertified products. What should I do?"
    menu:
        "Educate customers about safety.":
            $ customer_education = True
            jump branch_educate
        "Confront Sharma Ji.":
            $ customer_education = False
            jump branch_confront

# Branch 3A: Educate Customers
label branch_educate:
    show nisha smile 
    n "(handing out pamphlets) Did you know uncertified power banks can catch fire?"
    "A customer nods in agreement."
    show nisha smile at left with move
    show anand smile at right
    a "I’m sharing your store on social media. Safety matters!"
    
    "Community support starts to build around Nisha’s commitment to quality."
    
    jump scene4_meeting_priya

# Branch 3B: Confront Sharma Ji
label branch_confront:
    show nisha angry
    n "(angry) You’re selling junk! Someone could get hurt!"
    show nisha angry at left with move
    show sharma angry at right
    s "(scoffing) Worry about your own bills, Nisha."
    n "And let you fool these innocent people."
    s "Shut up! You better watch your back."
    "The argument goes viral. Sales dip temporarily, but the media brings CRS into the spotlight."
    
    jump scene4_meeting_priya

# Scene 4: Meeting Priya
label scene4_meeting_priya:

    scene bg office with fade
    "Inside a BIS office, Priya—a no-nonsense official—reviews files at her desk."
    show priya normal
    p "(leaning forward, empathetic) Ms. Nisha, I’ve reviewed your case. It’s admirable that you’re pursuing compliance after the notice. Many vendors ignore warnings until accidents happen."
    show priya normal at right with move
    show nisha sad at left
    n "(voice trembling) Thank you, Madam.{w} But compliance costs—lab tests, certified suppliers—it’s bleeding my savings. I have built this business from nothing. I can’t let it collapse."
    p "(softening) BIS isn’t here to punish you...{w} we’re here to prevent tragedies. Let’s find a way forward."
    p "Also, we have issued a notice against your previous supplier, they’ll be facing the consequences soon. I’m glad you’ve changed suppliers."
    n "Is there any way I can get out of this mess and save my business?"
    p "Full compliance now. Recall the non-CRS stock. Pay the penalties, and you’re all good."

    menu:
        "I’ll comply immediately. My customers’ safety comes first.":
            $ compliance = True
            show nisha smile
            n "(hands shaking, signing the compliance form) I’ll do it. Safety must come before profits."
            show priya smile
            p "(nodding) A brave choice. I’ll fast-track your application. Here’s a list of subsidized labs."
            n "Thankyou so much ma'am."
            jump scene5_crisis
        "I can’t commit to these costs right now; I’ll wait for a better solution.":
            $ compliance = False
            n "(firm but worried) I’m sorry, but I can’t commit to these costs immediately. We’ll continue operations for now."
            show priya angry
            p "(raising an eyebrow, voice steady) Ms. Nisha, BIS doesn’t work on promises. Non-compliance means your products will be flagged soon...{w} leading to seizures and steep fines."
            n "I have no other choice ma'am."
            jump scene5_crisis

# Scene 5: The Crisis
label scene5_crisis: 

    scene bg shop with fade
    "Few days later, an angry customer storms in holding a burnt power bank."
    
    show customer
    cu "(yelling) This burned my desk! You’ll pay for this!"
    show customer at left with move
    show nisha sad at right
    n "What happened sir?"
    cu "I bought this powerbank from your company a month ago, and it caught fire while I was charging it."
    n "We are really sorry sir. We'll replace it with a new one."
    cu "No, I don't want replacement, you will suffer for fooling your customers."
    hide customer
    scene bg shop with fade
    show das angry at left
    show nisha sad at right
    ad "(coldly) Ms. Nisha, we’ve had three complaints this week on the powerbanks of your brand. Show me your CRS certificates. Now."
    
    menu:
        "Blame the supplier.":
            $ acceptance = False
            n "(defensive) It’s the supplier’s fault! We’re victims here too!"
            if not (notice_investigated):
                ad "You received a notice from BIS but you ignored it, you dont want to be saved."
                n "No sir, give me a chance to fix this."
                ad "That notice was your chance. I can't help you now."
            elif not (good_supplier):
                ad "You didn’t change your supplier, you received a notice from BIS warning you, but you chose your profits."
                n "No sir, give me a chance to fix this."
                ad "That was your chance, you didn't even try to make things right. I can't help you now."
            else:
                ad "But the powerbank was of your company, so you'll need to face the consequences."
                n "No sir, give me a chance to fix this."
                show das normal
                ad "I can't do anything."
            scene bg shop_empty
            show nisha sad
            "Nisha's business and shop shuts down, she faces lawsuits by customers and is supposed to pay a hefty fine."
            "Ending: The Fall of Nisha’s Business."
            jump end_game
        "Apologize and recall the products.":
            $ acceptance = True
            if not (notice_investigated):
                ad "You received a notice from BIS but you ignored it, you dont want to be saved."
                n "No sir, give me a chance to fix this."
                ad "That notice was your chance. I can't help you now."
                scene bg shop_empty
                show nisha sad
                "Nisha's business and shop shuts down, she faces lawsuits by customers and is supposed to pay a hefty fine."
                "Ending: The Fall of Nisha’s Business."
                jump end_game

            elif not (good_supplier):
                ad "You didn’t change your supplier, you received a notice from BIS warning you, but you chose your profits."
                n "No sir, give me a chance to fix this."
                ad "That was your chance, you didn't even try to make things right. I can't help you now."
                scene bg shop_empty
                show nisha sad
                "Nisha's business and shop shuts down, she faces lawsuits by customers and is supposed to pay a hefty fine."
                "Ending: The Fall of Nisha’s Business."
                jump end_game

            if compliance:
                n "(teary) Sir, I am sorry, we have already started recalling our faulty products, we are trying our best."
            else:
                n "(teary) Sir, I am sorry, we will start recalling our faulty products, we will try to fix everything."
            show das sad
            ad "(softening) I can’t undo the damage. As per norms, you’ll face either a hefty fine or business suspension after legal proceedings."
            hide das
            show nisha at center with move
            "Auditor Das leaves the shop, Nisha faces lawsuits, and a hefty fine is imposed on her."
            if customer_education:
                scene bg shop with fade
                show anand smile at left
                show nisha smile at center
                show rahul smile at right
                "But Anand and other customers who noticed her advertising for certified products come in her support."
                "Nisha's business is saved due to her realising her mistakes and making efforts to correct them."
            elif compliance:
                scene bg shop with fade
                show nisha sad at left
                show rahul sad at right
                "Nisha suffers losses but her business survives."
            else:
                scene bg shop with fade
                show nisha sad at left
                show rahul sad at right
                "Nisha suffers losses, but she retains her integrity."
            jump end_game

label end_game:
    "THE END"
    return
