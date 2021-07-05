import pygame
import sys
import random
import math


pygame.init()
screen_width = 1100
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Donald Trump\'s Presidency')


#basic time

cover_time = 1000
cover_time1 = 1000
cover_time2 = 1000
cover_time3 = 1000
cover_time4 = 1000
cover_time5 = 5000

cover_time6 = 3000
cover_time7 = 3000
cover_time8 = 5000

gameover_time = 500
fadeout_time = 300


instruction_time = 2000
instruction_time2 = 5000

#enabling of clearing feature. Press 1 to clear by winning, Press 2 to clear by losing
#clearing features is enabled when clear = 1

clear = 1


#-------Chapter 1 Parameters-------#

trump_life = 200
energy_threshold = 200
reload_threshold = 10


hillary_life = 200

tweet_speed = [10,0]
email_speed = [50,0]
tax_return_speed = [-10,0]
audio_speed = [-20,0]


hillary_basic_speed = 15
hillary_frequency1 = 50  #tax return frequency
hillary_frequency2 = 80  #audio frequency

tweet_damage = 5
email_damage = 30
tax_return_damage = 5
audio_damage = 10

crooked_time = 80
show_email_time = 40
show_return_time = 20
grab_pussy_time = 30


z = crooked_time + 1
y = show_email_time + 1
m = show_return_time + 1
n = grab_pussy_time + 1

crooked_audio_charge = 0
emails_audio_charge = 0
taxreturns_audio_charge = 0

sound_frequency = 50


#-------Chapter 2 Parameters-------#

#----------Anger----------#
anger_threshold = 100
anger_warning_threshold = 80
block_immigrant_anger = 5
block_truck_anger = 5
emergency_anger = 10
lockup_anger = 20


#----------Count----------#
count_threshold = 40


#----------Security----------#
security = 150
security_warning_threshold = 20
illegal_immigrant_damage = 5
legal_immigrant_damage = 0
illegal_truck_damage = 10
legal_truck_damage = 0
dealer_damage = 20


#----------chapter2_border and Ports----------#
port_number = 2
border_position = screen_height * 0.2


#----------Patrols----------#
patrol_deploy_threshold = 10
patrol_position = 0, border_position + 10
patrol_speed = [20,0]
deploy_time_limit = 150
deploy_frequency = 15

#----------Lockups---------#
lockup_time_limit = 100
lockup_speed = 40

lockup_frequency_limit = 150
cage_positionx = 200
cage_positiony = screen_height - 200

#----------Emergency---------#
emergency_time_limit = 400
emergency_frequency_limit = 450

#----------Court Orders----------#
court_order_frequency = 30
court_order_time = 0
court_order_time_limit = 300


#----------Immigrants----------#
immigrant_frequency = 55
immigrant_speed_value = 7
horizontal_displacement = 10
angle_range = 30

#----------Trucks----------#
truck_frequency = 80
truck_speed_value = 10

#----------Dealers----------#
dealer_frequency = 10000000000
dealer_speed_value = 15


#----------Trump----------#
border_trump_speed = 20
wall_thickness = 60
vertical_activity_max = border_position + wall_thickness + 200



#-------Chapter 3 Parameters-------#

trump_height = 200
row_spacing = (screen_height - trump_height) / 3
column_spacing = screen_width/4

frequency1 = 20
news_time = 50
fakenews_time = 20
points_threshold = 20
fakenews_damage = 2
foxnews_add = 1



#-------Chapter 4 Parameters-------#

senator_width = 80
senator_height = 200

displacement = 250
fraction = 6
deltax = screen_width/2 - screen_width/fraction
deltay = screen_height - displacement

unit_vectorx = deltax / math.sqrt(deltax**2 + deltay**2)
unit_vectory = deltay / math.sqrt(deltax**2 + deltay**2)

speed_value = 8
frequency = 27

speed1 = [-(unit_vectorx*speed_value),(unit_vectory*speed_value)]
speed2 = [0,(unit_vectory*speed_value)]
speed3 = [(unit_vectorx*speed_value),(unit_vectory*speed_value)]
speeds = [speed1, speed2, speed3]

term_limit = 4
term_speed = 0.5


#-------Functions to help loading-------#
def load_and_scale(directory, w, h):
    image = pygame.image.load(directory)
    image.convert_alpha()
    image = pygame.transform.smoothscale(image, (w,h))
    return image

def load_scale_pos_center(directory, w, h, x, y):
    image = pygame.image.load(directory)
    image.convert_alpha()
    image = pygame.transform.smoothscale(image, (w, h))
    image_position = image.get_rect()
    image_position.center = x, y
    return(image, image_position)

def load_scale_getpos(directory, w, h):
    image = pygame.image.load(directory)
    image.convert_alpha()
    image = pygame.transform.smoothscale(image, (w, h))
    image_position = image.get_rect()
    return(image, image_position)

#-------Audio Files-------#
crooked_audio = pygame.mixer.Sound('assets/chapter1_media_war/crooked.wav')
emails_audio = pygame.mixer.Sound('assets/chapter1_media_war/emails.wav')
taxreturns_audio = pygame.mixer.Sound('assets/chapter1_media_war/taxreturns.wav')
fakenews_audio = pygame.mixer.Sound('assets/chapter3_fake_news/fakenews.wav')
stop_audio = pygame.mixer.Sound('assets/chapter4_impeachment/stop.wav')
cheers_audio = pygame.mixer.Sound('assets/chapter1_media_war/cheers.wav')
impeached_audio = pygame.mixer.Sound('assets/chapter4_impeachment/impeached.wav')

emergency_audio = pygame.mixer.Sound('assets/chapter2_border/emergency.wav')
patrol_audio = pygame.mixer.Sound('assets/chapter2_border/patrol.wav')
patrol_audio.set_volume(0.8)
lockup_audio = pygame.mixer.Sound('assets/chapter2_border/lockup.wav')
lockup_audio.set_volume(0.40)
protest_audio = pygame.mixer.Sound('assets/chapter2_border/protest.wav')
riot_audio = pygame.mixer.Sound('assets/chapter2_border/riot.wav')



#-------Fonts-------#

# Chapter 1
chapter1_font = pygame.font.Font(None,60)
chapter1_text = chapter1_font.render('CHAPTER 1',True,(255,0,0))
chapter1_text_position = chapter1_text.get_rect()
chapter1_text_position.center = screen_width/2, screen_height/2


donald_vs_crooked_font = pygame.font.Font(None,60)
donald_vs_crooked_text = donald_vs_crooked_font.render('DONALD VS CROOKED',True,(255,0,0))
donald_vs_crooked_text_position = donald_vs_crooked_text.get_rect()
donald_vs_crooked_text_position.center = screen_width/2, screen_height/2 + 50


won1_font = pygame.font.Font(None,60)
won1_text = won1_font.render('You Won!', True, (255,0,0))
won1_position = won1_text.get_rect()
won1_position.center = (screen_width/2, screen_height/2)



text1 = 'YOU DEFEATED HILLARY CLINTON'
text2 = 'AND BECAME PRESIDENT OF THE UNITED STATES!'
trumpvictory_font = pygame.font.Font(None,60)
trumpvictory_text = trumpvictory_font.render(text1, True, (255,0,0))
trumpvictory_position = trumpvictory_text.get_rect()
trumpvictory_position.center = (screen_width/2, screen_height/2)
trumpvictory2_font = pygame.font.Font(None,60)
trumpvictory2_text = trumpvictory2_font.render(text2, True, (255,0,0))
trumpvictory2_position = trumpvictory2_text.get_rect()
trumpvictory2_position.center = (screen_width/2, screen_height/2+60)


text3 = 'YOU LOST TO HILLARY CLINTON!'
hillaryvictory_font = pygame.font.Font(None,60)
hillaryvictory_text = hillaryvictory_font.render(text3, True, (0,0,255))
hillaryvictory_position = hillaryvictory_text.get_rect()
hillaryvictory_position.center = (screen_width/2, screen_height/2)


gameover_font = pygame.font.Font(None,60)
gameover_text = gameover_font.render('GAME OVER!', True, (0,0,255))
gameover_position = gameover_text.get_rect()
gameover_position.center = (screen_width/2, screen_height/2+50)


# Chapter 2

chapter2_font = pygame.font.Font(None,60)
chapter2_text = chapter2_font.render('CHAPTER 2',True,(255,0,0))
chapter2_text_position = chapter2_text.get_rect()
chapter2_text_position.center = screen_width/2, screen_height/2


immigration_war_font = pygame.font.Font(None,60)
immigration_war_text = immigration_war_font.render('THE WAR AGAINST ILLEGAL IMMIGRANTS',True,(255,0,0))
immigration_war_text_position = immigration_war_text.get_rect()
immigration_war_text_position.center = screen_width/2, screen_height/2 + 50


anger_font = pygame.font.Font(None, 50)
anger_text = anger_font.render('YOUR INHUMANE BORDER POLICIES', True, (255,0,0))
anger_text_position = anger_text.get_rect()
anger_text_position.center = screen_width/2, screen_height/2 -50

anger1_font = pygame.font.Font(None, 50)
anger1_text = anger1_font.render('ENRAGED THE AMERICAN PEOPLE', True, (255,0,0))
anger1_text_position = anger1_text.get_rect()
anger1_text_position.center = screen_width/2, screen_height/2

anger2_font = pygame.font.Font(None, 55)
anger2_text = anger2_font.render('YOU WERE KICKED OUT OF THE UNITED STATES!', True, (255,0,0))
anger2_text_position = anger2_text.get_rect()
anger2_text_position.center = screen_width/2, screen_height/2 + 50

security1_font = pygame.font.Font(None, 45)
security1_text = security1_font.render('ILLEGAL IMMIGRANTS DESTROYED NATIONAL SECURITY', True, (255,0,0))
security1_text_position = security1_text.get_rect()
security1_text_position.center = screen_width/2, screen_height/2

security2_font = pygame.font.Font(None, 60)
security2_text = security2_font.render('THE UNITED STATES IS NOW IN CHAOS!', True, (255,0,0))
security2_text_position = security2_text.get_rect()
security2_text_position.center = screen_width/2, screen_height/2 + 50

mexico_font = pygame.font.Font(None, 40)
mexico_text = mexico_font.render('YOUR DETERMINATION IN CRACKING DOWN ON IMMIGRATION', True, (255,0,0))
mexico_text_position = mexico_text.get_rect()
mexico_text_position.center = screen_width/2, screen_height/2 -40

mexico1_font = pygame.font.Font(None, 40)
mexico1_text = mexico1_font.render('TOUCHED THE MEXICAN PRESIDENT', True, (255,0,0))
mexico1_text_position = mexico1_text.get_rect()
mexico1_text_position.center = screen_width/2, screen_height/2 

mexico2_font = pygame.font.Font(None, 60)
mexico2_text = mexico2_font.render('AND HE DECIDED TO PAY FOR YOUR WALL!', True, (255,0,0))
mexico2_text_position = mexico2_text.get_rect()
mexico2_text_position.center = screen_width/2, screen_height/2 + 40


# Chapter 3

chapter3_font = pygame.font.Font(None,60)
chapter3_text = chapter3_font.render('CHAPTER 3',True,(255,0,0))
chapter3_text_position = chapter3_text.get_rect()
chapter3_text_position.center = screen_width/2, screen_height/2 


media_war_font = pygame.font.Font(None,60)
media_war_text = media_war_font.render('TRUMP\'S WAR WITH THE MEDIA',True,(255,0,0))
media_war_text_position = media_war_text.get_rect()
media_war_text_position.center = screen_width/2, screen_height/2 + 50


lost_font = pygame.font.Font(None,60)
lost_text = lost_font.render('YOUR RATINGS HAVE FALLEN TO ZERO',True,(0,0,255))
lost_text_position = lost_text.get_rect()
lost_text_position.center = screen_width/2, screen_height/2 


lost2_font = pygame.font.Font(None,60)
lost2_text = lost2_font.render('NANCY PELOSI DECIDED TO IMPEACH YOU!',True,(0,0,255))
lost2_text_position = lost2_text.get_rect()
lost2_text_position.center = screen_width/2, screen_height/2 + 50


won_font = pygame.font.Font(None,60)
won_text = won_font.render('YOU WON THE WAR AGAINST THE MEDIA',True,(0,0,255))
won_text_position = won_text.get_rect()
won_text_position.center = screen_width/2, screen_height/2 


won2_font = pygame.font.Font(None,60)
won2_text = won2_font.render('BUT NANCY PELOSI DECIDED TO IMPEACH YOU!',True,(0,0,255))
won2_text_position = won2_text.get_rect()
won2_text_position.center = screen_width/2, screen_height/2 + 50


# Chapter 4

chapter4_font = pygame.font.Font(None,60)
chapter4_text = chapter4_font.render('CHAPTER 4',True,(255,0,0))
chapter4_text_position = chapter4_text.get_rect()
chapter4_text_position.center = screen_width/2, screen_height/2


impeachment_saga_font = pygame.font.Font(None,60)
impeachment_saga_text = impeachment_saga_font.render('THE IMPEACHMENT SAGA',True,(255,0,0))
impeachment_saga_text_position = impeachment_saga_text.get_rect()
impeachment_saga_text_position.center = screen_width/2, screen_height/2 + 50


            
avoided_font = pygame.font.Font(None,60)
avoided_text = avoided_font.render('YOU SUCCESSFULL AVOIDED IMPEACHMENT',True,(0,0,255))
avoided_text_position = avoided_text.get_rect()
avoided_text_position.center = screen_width/2, screen_height/2 -50


retired_font = pygame.font.Font(None,60)
retired_text = retired_font.render('AND PEACEFULLY RETIRED!',True,(0,0,255))
retired_text_position = retired_text.get_rect()
retired_text_position.center = screen_width/2, screen_height/2

impeached_font = pygame.font.Font(None,55)
impeached_text = impeached_font.render('YOU WERE SUCCEFULLY IMPEACHED BY THE SENATE',True,(255,0,0))
impeached_text_position = impeached_text.get_rect()
impeached_text_position.center = screen_width/2, screen_height/2 -50


removed_font = pygame.font.Font(None,55)
removed_text = removed_font.render('AND REMOVED FROM OFFICE!',True,(255,0,0))
removed_text_position = removed_text.get_rect()
removed_text_position.center = screen_width/2, screen_height/2



#-------Title Pictures-------#

chapter1 = pygame.image.load('assets/game_assets/chapter1.png')
chapter1.convert_alpha()
#chapter1 = pygame.transform.smoothscale(chapter1,(screen_width,screen_height))
chapter1_position = chapter1.get_rect()
chapter1_position.center = screen_width/2, screen_height/2

chapter2_1, chapter2_1_position = load_scale_pos_center('assets/game_assets/chapter2_1.png', screen_width, screen_height, screen_width/2, screen_height/2)
chapter2_2, chapter2_2_position = load_scale_pos_center('assets/game_assets/chapter2_2.png', screen_width, screen_height, screen_width/2, screen_height/2)
chapter2_3, chapter2_3_position = load_scale_pos_center('assets/game_assets/chapter2_3.png', screen_width-80, screen_height, screen_width/2, screen_height/2)
chapter2_4, chapter2_4_position = load_scale_pos_center('assets/game_assets/chapter2_4.png', screen_width, screen_height, screen_width/2, screen_height/2)

chapter3, chapter3_position = load_scale_pos_center('assets/game_assets/chapter3.png', screen_width, screen_height, screen_width/2, screen_height/2)
chapter4, chapter4_position = load_scale_pos_center('assets/game_assets/chapter4.png', screen_width, screen_height, screen_width/2, screen_height/2)


#-------Image for Continue Button-------#
button_image, button_position = load_scale_pos_center('assets/game_assets/button.png', 180, 70, screen_width/2, screen_height * 0.8)

#-------Images for Instructions-------#
instructions1, instructions1_position = load_scale_pos_center('assets/game_assets/instructions1.png', screen_width, screen_height, screen_width/2, screen_height/2)
instructions2, instructions2_position = load_scale_pos_center('assets/game_assets/instructions2.png', screen_width, screen_height, screen_width/2, screen_height/2)
instructions3, instructions3_position = load_scale_pos_center('assets/game_assets/instructions3.png', screen_width, screen_height, screen_width/2, screen_height/2)
instructions4, instructions4_position = load_scale_pos_center('assets/game_assets/instructions4.png', screen_width, screen_height, screen_width/2, screen_height/2)


#-------Images: Cover Photos------#
trump_vs, trump_vs_position = load_scale_getpos('assets/chapter1_media_war/trump_vs_hillary.jpg', screen_width, screen_height)
rally, rally_position = load_scale_getpos('assets/chapter1_media_war/rally.jpeg', screen_width, screen_height)
rally.set_alpha(200)
hillary_rally, hillary_rally_position = load_scale_getpos('assets/chapter1_media_war/hillary_rally.jpg', screen_width, screen_height)

media_war, media_war_position = load_scale_getpos('assets/chapter3_fake_news/media_war.jpg', screen_width, screen_height)



impeach, impeach_position = load_scale_pos_center('assets/chapter3_fake_news/impeach.jpg', screen_width, screen_height, screen_width/2, screen_height/2)
trump_at_border_image, trump_at_border_position = load_scale_getpos('assets/chapter2_border/Pictures/trump_at_border.jpg', screen_width, screen_height)
trump_at_border_image.set_alpha(200)
anger_image = load_scale_getpos('assets/chapter2_border/Pictures/immigration_protest.jpg', screen_width, screen_height)[0]
anger_image.set_alpha(200)
security_image = load_scale_getpos('assets/chapter2_border/Pictures/riot2.jpg', screen_width, screen_height)[0]
security_image.set_alpha(200)
mexico_image = load_scale_getpos('assets/chapter2_border/Pictures/mexico.jpg', screen_width, screen_height)[0]
mexico_image.set_alpha(200)


trial = pygame.image.load('assets/chapter4_impeachment/trial2.jpg')
trial.convert()
trial = pygame.transform.smoothscale(trial,(screen_width,screen_height))


impeached = pygame.image.load('assets/chapter4_impeachment/impeached.jpg')
impeached.convert()
impeached = pygame.transform.smoothscale(impeached,(screen_width,screen_height))

retired = pygame.image.load('assets/chapter4_impeachment/retire.jpg')
retired.convert()
retired = pygame.transform.smoothscale(retired,(screen_width,screen_height))

#-------Images: Background Photos------#
debate_stage = pygame.image.load('assets/chapter1_media_war/debate_stage.jpg')
debate_stage.convert()
debate_stage = pygame.transform.smoothscale(debate_stage, (screen_width,screen_height))
debate_stage.set_alpha(150)
debate_stage_position = debate_stage.get_rect()

desert_image = pygame.image.load('assets/chapter2_border/Pictures/desert3.jpg')
desert_image.convert()
desert_image = pygame.transform.smoothscale(desert_image, (screen_width, screen_height))

congress = pygame.image.load('assets/chapter4_impeachment/congress2.jpg')
congress.convert()
congress = pygame.transform.smoothscale(congress,(screen_width, screen_height))




#-------Images: Chapter 1------#

email_image = load_and_scale('assets/chapter1_media_war/email.png', 100, 100)

#email_image = pygame.image.load('assets/chapter1_media_war/email.png')
#email_image.convert_alpha()
#email_image = pygame.transform.smoothscale(email_image,(100,100))

tweet_image = pygame.image.load('assets/chapter1_media_war/tweet.png')
tweet_image.convert_alpha()
tweet_image = pygame.transform.smoothscale(tweet_image,(180,90))

tax_return_image = pygame.image.load('assets/chapter1_media_war/tax_return.png')
tax_return_image.convert_alpha()
tax_return_image = pygame.transform.smoothscale(tax_return_image,(80,100))

audio_image = pygame.image.load('assets/chapter1_media_war/audio2.png')
audio_image.convert_alpha()
audio_image = pygame.transform.smoothscale(audio_image,(100,120))

trump1_image = pygame.image.load('assets/chapter1_media_war/trump4.png')
trump1_image.convert_alpha()
trump1_image = pygame.transform.smoothscale(trump1_image,(360,220))
trump1_image_position = trump1_image.get_rect()
trump1_image_position.center = 0, screen_height/2
trump1_image_position.left = 0

hillary_image = pygame.image.load('assets/chapter1_media_war/hillary.png')
hillary_image.convert_alpha()
hillary_image = pygame.transform.smoothscale(hillary_image,(360,220))
hillary_image_position = hillary_image.get_rect()
hillary_image_position.center = screen_width, screen_height/2
hillary_image_position.right = screen_width

crooked = pygame.image.load('assets/chapter1_media_war/crooked.png')
crooked.convert_alpha()
crooked = pygame.transform.smoothscale(crooked,(300,175))

show_email = pygame.image.load('assets/chapter1_media_war/show_email.png')
show_email.convert_alpha()
show_email = pygame.transform.smoothscale(show_email,(300,175))

show_return = pygame.image.load('assets/chapter1_media_war/show_return.png')
show_return.convert_alpha()
show_return = pygame.transform.smoothscale(show_return,(300,175))

grab_pussy = pygame.image.load('assets/chapter1_media_war/grab_pussy.png')
grab_pussy.convert_alpha()
grab_pussy = pygame.transform.smoothscale(grab_pussy,(300,175))



#-------Images: Chapter 2------#



trump4_image = pygame.image.load('assets/chapter2_border/Pictures/trump_border2.png')
trump4_image.convert_alpha()
trump4_image = pygame.transform.smoothscale(trump4_image,(140,150))

immigrant_image = pygame.image.load('assets/chapter2_border/Pictures/immigrant.png')
immigrant_image.convert_alpha()
immigrant_image = pygame.transform.smoothscale(immigrant_image,(120,100))

legal_immigrant_image = pygame.image.load('assets/chapter2_border/Pictures/legal_immigrant.png')
legal_immigrant_image.convert_alpha()
legal_immigrant_image = pygame.transform.smoothscale(legal_immigrant_image,(120,100))

truck_image = pygame.image.load('assets/chapter2_border/Pictures/truck.png')
truck_image.convert_alpha()
truck_image = pygame.transform.smoothscale(truck_image, (50,130))

legal_truck_image = pygame.image.load('assets/chapter2_border/Pictures/legal_truck.png')
legal_truck_image.convert_alpha()
legal_truck_image = pygame.transform.smoothscale(legal_truck_image, (50,130))

dealer_image = pygame.image.load('assets/chapter2_border/Pictures/drug_dealer.png')
dealer_image.convert_alpha()
dealer_image = pygame.transform.smoothscale(dealer_image, (100,100))

wall_long_image = pygame.image.load('assets/chapter2_border/Pictures/wall_long.png')
wall_long_image.convert_alpha()
wall_long_image = pygame.transform.smoothscale(wall_long_image, (500,wall_thickness))

wall_short_image = pygame.image.load('assets/chapter2_border/Pictures/wall_short.png')
wall_short_image.convert_alpha()
wall_short_image = pygame.transform.smoothscale(wall_short_image, (250,wall_thickness))

port_image = pygame.image.load('assets/chapter2_border/Pictures/port.png')
port_image.convert_alpha()
port_image = pygame.transform.smoothscale(port_image, (100,80))

patrol_image = pygame.image.load('assets/chapter2_border/Pictures/border_patrol.png')
patrol_image.convert_alpha()
patrol_image = pygame.transform.smoothscale(patrol_image, (220,160))

court_order_image = pygame.image.load('assets/chapter2_border/Pictures/court_order2.jpg')
court_order_image.convert()
court_order_image = pygame.transform.smoothscale(court_order_image, (300,200))
court_order_position = court_order_image.get_rect()
court_order_position.center = screen_width/2, screen_height/2

cage_image = pygame.image.load('assets/chapter2_border/Pictures/cage1.png')
cage_image.convert_alpha()
cage_image = pygame.transform.smoothscale(cage_image,(200,200))
cage_position = cage_image.get_rect()
cage_position.center = cage_positionx, cage_positiony


border_line_image = pygame.image.load('assets/chapter2_border/Pictures/border_line.png')
border_line_image.convert_alpha()
border_line_image = pygame.transform.smoothscale(border_line_image, (screen_width, 20))



patrol_speechbox_image = pygame.image.load('assets/chapter2_border/Pictures/border_patrol_speechbox.png')
patrol_speechbox_image.convert_alpha()
patrol_speechbox_image = pygame.transform.smoothscale(patrol_speechbox_image, (140,120))

lockup_speechbox_image = pygame.image.load('assets/chapter2_border/Pictures/lockup_speechbox.png')
lockup_speechbox_image.convert_alpha()
lockup_speechbox_image = pygame.transform.smoothscale(lockup_speechbox_image, (140,120))

national_emergency_speechbox_image = pygame.image.load('assets/chapter2_border/Pictures/national_emergency_speechbox.png')
national_emergency_speechbox_image.convert_alpha()
national_emergency_speechbox_image = pygame.transform.smoothscale(national_emergency_speechbox_image, (220,140))



#-------Images: Chapter 3-------#

trump_press1 = pygame.image.load('assets/chapter3_fake_news/trump_conference1.jpg')
trump_press1.convert()
trump_press1 = pygame.transform.smoothscale(trump_press1, (300,150))
trump_press1_position = trump_press1.get_rect()
trump_press1_position.center = (screen_width/2, screen_height/2)
trump_press1_position.top = 0

media_images = []
                        

chair_image = pygame.image.load('assets/chapter3_fake_news/chair2.png')
chair_image.convert_alpha()


cnn_image = pygame.image.load('assets/chapter3_fake_news/cnn.png')
cnn_image.convert_alpha()
media_images.append(cnn_image)

nyt_image = pygame.image.load('assets/chapter3_fake_news/nyt.jpg')
nyt_image.convert_alpha()
media_images.append(nyt_image)

washingtonpost_image = pygame.image.load('assets/chapter3_fake_news/washingtonpost.jpg')
washingtonpost_image.convert_alpha()
media_images.append(washingtonpost_image)

foxnews_image = pygame.image.load('assets/chapter3_fake_news/foxnews.jpg')
foxnews_image.convert_alpha()
media_images.append(foxnews_image)

fakenews_image = pygame.image.load('assets/chapter3_fake_news/fakenews.png')
fakenews_image.convert_alpha()


#-------Images: Chapter 4-------#
trump3 = pygame.image.load('assets/chapter4_impeachment/trump.png')
trump3.convert_alpha()
trump3 = pygame.transform.smoothscale(trump3,(210,135))
trump3_position = trump3.get_rect()
trump3_position.center = screen_width/2, screen_height/2
trump3_position.bottom = screen_height


bernie_image = pygame.image.load('assets/chapter4_impeachment/bernie.png')
bernie_image.convert_alpha()
bernie_image = pygame.transform.smoothscale(bernie_image,(100,250))


chuck_image = pygame.image.load('assets/chapter4_impeachment/chuck.png')
chuck_image.convert_alpha()
chuck_image = pygame.transform.smoothscale(chuck_image,(100,200))

cory_image = pygame.image.load('assets/chapter4_impeachment/cory.png')
cory_image.convert_alpha()
cory_image = pygame.transform.smoothscale(cory_image,(100,200))


kamala_image = pygame.image.load('assets/chapter4_impeachment/kamala.png')
kamala_image.convert_alpha()
kamala_image = pygame.transform.smoothscale(kamala_image,(175,280))

warren_image = pygame.image.load('assets/chapter4_impeachment/warren.png')
warren_image.convert_alpha()
warren_image = pygame.transform.smoothscale(warren_image,(140, 200))

nancy_image = pygame.image.load('assets/chapter4_impeachment/nancy.png')
nancy_image.convert_alpha()
nancy_image = pygame.transform.smoothscale(nancy_image,(90,215))
    

mitch_image = pygame.image.load('assets/chapter4_impeachment/mitch.png')
mitch_image.convert_alpha()
mitch_image = pygame.transform.smoothscale(mitch_image,(140,171))

ted_image = pygame.image.load('assets/chapter4_impeachment/ted.png')
ted_image.convert_alpha()
#ted_image = pygame.transform.smoothscale(ted_image,(senator_width,senator_height))




emails = []
tweets = [] 
tax_returns = []
audios = []
burgers = []

emails_group = pygame.sprite.Group()
tweets_group = pygame.sprite.Group()
tax_returns_group  = pygame.sprite.Group()
audios_group = pygame.sprite.Group()
burgers_group = pygame.sprite.Group()


class Hamburger(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.image.left, self.image.top = position


class Object(pygame.sprite.Sprite):
    def __init__(self, image, position,speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image) ####creating a mask
    def move(self):
        self.rect = self.rect.move(self.speed)

i = 0 
trump_reload = 0
trump_energy = 0
trump_speed = [0,0]



hillary = Object(hillary_image, (hillary_image_position.left, hillary_image_position.top), [0,0])
trump1 = Object(trump1_image, (trump1_image_position.left, trump1_image_position.top), [0,0])


end_chapter1_intro1 = False
while not end_chapter1_intro1:
    screen.blit(trump_vs, trump_vs_position)
    screen.blit(chapter1_text, chapter1_text_position)
    screen.blit(media_war_text,media_war_text_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter1_intro1 = True
                break

end_chapter1_intro2 = False
while not end_chapter1_intro2:
    screen.blit(chapter1,chapter1_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter1_intro2 = True
                break

end_chapter1_intro3 = False
while not end_chapter1_intro3:
    screen.blit(instructions1,instructions1_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter1_intro3 = True
                break     


while hillary_life > 0 and trump_life > 0:
    crooked_audio_charge += 1
    emails_audio_charge += 1
    taxreturns_audio_charge += 1

    if crooked_audio_charge >= sound_frequency:
        crooked_audio_charge = sound_frequency
    if emails_audio_charge >= sound_frequency:
        emails_audio_charge = sound_frequency
    if emails_audio_charge >= sound_frequency:
        emails_audio_charge = sound_frequency         
        
    screen.blit(debate_stage,debate_stage_position)
    
    i += 1
    z += 1
    y += 1
    m += 1
    n += 1
    trump_reload += 1
    trump_energy += 1
    if trump_energy > energy_threshold:
        trump_energy = energy_threshold
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if clear == 1:
                if event.key == 57:
                    hillary_life = 0 
                if event.key == 48:
                    trump_life = 0
                
            if event.key == 119:
                trump1.speed = [0,-10]
            if event.key == 115:
                trump1.speed = [0, 10]
            if event.key == 97:
                trump1.speed = [-10,0]
            if event.key == 100:
                trump1.speed = [10,0]

            if event.key == 32:
                if trump_reload >= reload_threshold:
                    tweet_init_position = trump1.rect.left+20, trump1.rect.top - 20    
                    tweet = Object(tweet_image, tweet_init_position, tweet_speed)
                    tweets_group.add(tweet)
                    tweets.append(tweet)
                    if crooked_audio_charge >= sound_frequency:
                        
                        crooked_audio.play()
                        crooked_audio_charge = 0
                    z = 0
                    trump_reload = 0


            if event.key == 13:
                if trump_energy == energy_threshold:
                    if emails_audio_charge >= sound_frequency:
                        emails_audio.play()
                        emails_audio_charge = 0
                    email_init_position = trump1.rect.left+20, trump1.rect.top - 20
                    email = Object(email_image, email_init_position, email_speed)
                    emails_group.add(email)
                    emails.append(email)
                    trump_energy = 0
                    y = 0

                    #show_email_position = trump_position.left+180, trump_position.top - 80

        if event.type == pygame.KEYUP:
            trump1.speed = [0,0]




    if i%50 == 1:
        x = random.choice([1,2,3,4,5,6,7,8])

    if x == 1:
        hillary.speed = [0,-hillary_basic_speed]
    if x == 2:
        hillary.speed = [hillary_basic_speed,-hillary_basic_speed]
    if x == 3:
        hillary.speed = [hillary_basic_speed,0]
    if x == 4:
        hillary.speed = [hillary_basic_speed,hillary_basic_speed]           
    if x == 5:
        hillary.speed = [0,hillary_basic_speed]                    
    if x == 6:
        hillary.speed = [-hillary_basic_speed,hillary_basic_speed]
    if x == 7:
        hillary.speed = [-hillary_basic_speed,0]           
    if x == 8:
        hillary.speed = [-hillary_basic_speed,-hillary_basic_speed]
                

    trump1.move()
    if trump1.rect.right > screen_width*0.4:
        trump1.rect.right = screen_width*0.4
    if trump1.rect.left < 0:
        trump1.rect.left = 0
    if trump1.rect.bottom > screen_height:
        trump1.rect.bottom = screen_height
    if trump1.rect.top < 0:
        trump1.rect.top = 0
    screen.blit(trump1.image,trump1.rect)

    if z <= crooked_time:
        crooked_position = trump1.rect.left+180, trump1.rect.top - 40
        screen.blit(crooked,crooked_position)

    if y <= show_email_time:
        show_email_position = trump1.rect.left+180, trump1.rect.top - 40
        screen.blit(show_email, show_email_position)

    
    hillary.move()
    if hillary.rect.right > screen_width:
        hillary.rect.right = screen_width
    if hillary.rect.left < screen_width*0.6:
        hillary.rect.left = screen_width*0.6
    if hillary.rect.bottom > screen_height:
        hillary.rect.bottom = screen_height
    if hillary.rect.top < 0:
        hillary.rect.top = 0
    screen.blit(hillary.image,hillary.rect)

    if i%hillary_frequency1 == hillary_frequency1 - 1:
        
        tax_return_init_position = hillary.rect.left-20, hillary.rect.top+20    
        tax_return = Object(tax_return_image, tax_return_init_position, tax_return_speed)
        tax_returns.append(tax_return)
        tax_returns_group.add(tax_return)
        if taxreturns_audio_charge >= sound_frequency:
            if random.randint(0,2) == 1:
                taxreturns_audio.play()
                taxreturns_audio_charge = 0
        
        m = 0

    if m <= show_return_time:
        show_return_position = hillary.rect.left-40, hillary.rect.top-20
        screen.blit(show_return,show_return_position)


    if i%hillary_frequency2 == hillary_frequency2 - 2:
        
        audio_init_position = hillary.rect.left-20, hillary.rect.top+20    
        audio = Object(audio_image, audio_init_position, audio_speed)
        audios.append(audio)
        audios_group.add(audio)
        n = 0

    if n <= grab_pussy_time:
        grab_pussy_position = hillary.rect.left-40, hillary.rect.top-20
        screen.blit(grab_pussy, grab_pussy_position)   


    for tweet in tweets_group:
        tweet.move()
        screen.blit(tweet.image,tweet.rect)

    for email in emails_group:
        email.move()
        screen.blit(email.image,email.rect)

    for tax_return in tax_returns_group:
        tax_return.move()
        screen.blit(tax_return.image,tax_return.rect)

    for audio in audios_group:
        audio.move()
        screen.blit(audio.image,audio.rect)

    collide_list1 = pygame.sprite.spritecollide(hillary, tweets_group, True, pygame.sprite.collide_mask)
    hillary_life -= len(collide_list1) * tweet_damage
    
    for tweet in tweets_group:
        if tweet.rect.left > screen_width:
            tweets.remove(tweet)
            tweets_group.remove(tweet)

    collide_list2 = pygame.sprite.spritecollide(hillary, emails_group, True, pygame.sprite.collide_mask)
    hillary_life -= len(collide_list2) * email_damage
    
    for email in emails_group:
        if email.rect.left > screen_width:
            emails.remove(email)
            emails_group.remove(email)

    collide_list3 = pygame.sprite.spritecollide(trump1, audios_group, True, pygame.sprite.collide_mask)
    trump_life -= len(collide_list3) * audio_damage
    for audio in audios_group:
        if audio.rect.right < 0:
            audios.remove(audio)
            audios_group.remove(audio)
            
    collide_list4 = pygame.sprite.spritecollide(trump1, tax_returns_group, True, pygame.sprite.collide_mask)
    trump_life -= len(collide_list4) * tax_return_damage
    
    for tax_return in tax_returns_group:
        if tax_return.rect.right < 0:
            tax_returns.remove(tax_return)
            tax_returns_group.remove(tax_return)
            

    if trump_life <= 0:
        trump_life = 0

        screen.blit(gameover_text,gameover_position)
        pygame.time.delay(gameover_time)

    if hillary_life <= 0:
        hillary_life = 0

        screen.blit(won1_text,won1_position)
        pygame.time.delay(gameover_time)

    trumplife_font = pygame.font.Font(None,40)
    trumplife_text = trumplife_font.render('Life: '+str(trump_life),True,(0,255,0))
    trumplife_position = (30,30)
    screen.blit(trumplife_text,trumplife_position)

    trumpenergy_font = pygame.font.Font(None,40)
    trumpenergy_text = trumpenergy_font.render('Energy: '+str(trump_energy),True,(0,255,0))
    
    if trump_energy == energy_threshold:
        trumpenergy_text = trumpenergy_font.render('Energy: '+str(trump_energy),True,(255,0,0))
    trumpenergy_position = (30,70)
    screen.blit(trumpenergy_text,trumpenergy_position)

    hillarylife_font = pygame.font.Font(None,40)
    hillarylife_text = hillarylife_font.render('Life: '+str(hillary_life),True,(0,255,0))
    hillarylife_position = (screen_width-140,30)
    screen.blit(hillarylife_text,hillarylife_position)

    pygame.display.flip()
    screen.fill((255,255,255))

    if hillary_life <= 0:
        cheers_audio.play()
        break


    if trump_life <= 0:
        screen.fill((255,255,255))
        screen.blit(hillary_rally,hillary_rally_position)


        screen.blit(hillaryvictory_text,hillaryvictory_position)
        screen.blit(gameover_text,gameover_position)
       
        pygame.display.flip()
        sys.exit()
        
end_chapter1_endscene = False
while not end_chapter1_endscene:
    screen.fill((255,255,255))
    screen.blit(rally, rally_position)
    screen.blit(trumpvictory_text,trumpvictory_position)
    screen.blit(trumpvictory2_text,trumpvictory2_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                cheers_audio.fadeout(fadeout_time)
                end_chapter1_endscene = True
                break    



screen.fill((255,255,255))




class Object(pygame.sprite.Sprite):
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position


chairs = []
news_positions = []
news_list = []
news_timeleft_list = []
news_timeleft_dict = {}
news_dict = {}

icons_dict = {}
icons_timeleft_dict = {}



for column in range(1,5):
    for row in range(1,4):  
        chair_position = column_spacing * (column-0.5) , row_spacing * (row-0.5) + trump_height
        chair = Object(chair_image,chair_position)
        chairs.append(chair)

        news_position = column_spacing * (column-0.5) , row_spacing * (row-0.5) - 50 + trump_height
        news_positions.append(news_position)

i = 0
k = -1


fakenews_audio_charge = 0
points = 0
ratings = 50

#####Chapter 2#####

class Trump(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.rect.bottom = position[1]
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)

class Wall(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.rect.bottom = position[1]


class Patrol(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.right, self.rect.top = position
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)

class Invader(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.right, self.rect.bottom = position
        self.speed = speed
        self.status = 'illegal'
        self.blocked = 0
        self.lockedup = 0

        
    def move(self):
        self.rect = self.rect.move(self.speed)       

class Port(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

immigrants = pygame.sprite.Group()
dealers = pygame.sprite.Group()
trucks = pygame.sprite.Group()
patrols = pygame.sprite.Group()
ports = pygame.sprite.Group()


anger = 0
count = 0
deploy_charge = 0
emergency_charge = 0
lockup_charge = 0
activated_list = [0]

i = 0
court_order_status = 0
emergency_time = emergency_time_limit + 1
deploy_time = deploy_time_limit +1
lockup_time = lockup_time_limit +1
border_trump = Trump(trump4_image, (screen_width/2, screen_height), [0,0])

#----------Generating and Blitting Ports----------#


port_distance = screen_width / (port_number + 1)
for j in range(1,port_number+1):
    port_position = j * port_distance, border_position
    port = Port(port_image, port_position)
    ports.add(port)


border_line_position = border_line_image.get_rect()
border_line_position.center = screen_width/2, border_position


end_chapter2_intro1 = False
while not end_chapter2_intro1:
    screen.fill((255,255,255))
    screen.blit(trump_at_border_image, trump_at_border_position)
    screen.blit(chapter2_text, chapter2_text_position)
    screen.blit(immigration_war_text, immigration_war_text_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_intro1 = True
                break    

end_chapter2_intro2 = False
while not end_chapter2_intro2:
    screen.fill((255,255,255))
    screen.blit(chapter2_1, chapter2_1_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_intro2 = True
                break    

end_chapter2_intro3 = False
while not end_chapter2_intro3:
    screen.fill((255,255,255))
    screen.blit(chapter2_2, chapter2_2_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_intro3 = True
                break   

end_chapter2_intro4 = False
while not end_chapter2_intro4:
    screen.fill((255,255,255))
    screen.blit(chapter2_3, chapter2_3_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_intro4 = True
                break  

end_chapter2_intro5 = False
while not end_chapter2_intro5:
    screen.fill((255,255,255))
    screen.blit(chapter2_4, chapter2_4_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_intro5 = True
                break  

end_chapter2_intro5 = False
while not end_chapter2_intro5:
    screen.fill((255,255,255))
    screen.blit(instructions2, instructions2_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_intro5 = True
                break

while True:
 
    i += 1
    screen.blit(desert_image, (0,0))
    screen.blit(border_line_image, border_line_position)
    
    for port in ports:
        screen.blit(port.image, port.rect)


    #----------Court Order Issued upon Increased Anger---------#
    
    activated_times = int(anger/court_order_frequency)
    #anger_backup = anger - activated_times * court_order_frequency
   
    if activated_times > max(activated_list):
        activated_list.append(activated_times)
        court_order_status = 1
        court_order_time = 0
        lockup_time = lockup_time_limit +1
        
        
    court_order_time += 1
    if court_order_time > court_order_time_limit:
        court_order_status = 0
    
        

    #----------Controlling Trump----------#

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:         
            if event.key == 119:
                border_trump.speed = [0,-border_trump_speed]
            if event.key == 115:
                border_trump.speed = [0, border_trump_speed]
            if event.key == 97:
                border_trump.speed = [-border_trump_speed,0]
            if event.key == 100:
                border_trump.speed = [border_trump_speed,0]
            if event.key == 49:
                if deploy_charge >= patrol_deploy_threshold:
                    deploy_time = 0
                    deploy_charge = 0
                    patrol_audio.play()
            if event.key == 51:
                if lockup_charge >= lockup_frequency_limit and court_order_status == 0:
                    lockup_charge = 0
                    anger += lockup_anger
                    lockup_time = 0
                    lockup_audio.play()
                    
            if clear == 1:
                if event.key == 57:
                    count = count_threshold
                if event.key == 48:
                    security = 0
                

            if event.key == 50:
                if emergency_charge >= emergency_frequency_limit and court_order_status == 0:
                    emergency_charge = 0
                    anger += emergency_anger
                    emergency_time = 0
                    emergency_audio.play()

             
        if event.type == pygame.KEYUP:
            if event.key == 119 or event.key == 115 or event.key == 97 or event.key == 100:
                border_trump.speed = [0,0]

    emergency_charge += 1
    lockup_charge += 1


    #trump can't move when court order is in effect
    
    if court_order_status == 1:
        border_trump.speed = [0,0]
        lockup_time = lockup_time_limit +1
    
    
    border_trump.move()
    
    if border_trump.rect.bottom > screen_height:
        border_trump.rect.bottom = screen_height
    if border_trump.rect.top < vertical_activity_max:
        border_trump.rect.top = vertical_activity_max
    if border_trump.rect.left < -50:
        border_trump.rect.left = -50
    if border_trump.rect.right > screen_width+50:
        border_trump.rect.right = screen_width+50
    

    #----------Generating Invaders----------#
    #Generating Immigrants

    if i % immigrant_frequency == immigrant_frequency -1:

        immigrant_position_init = random.randint(0,screen_width), 0

        unit_vector = pygame.math.Vector2(0,1)
        angle = random.randint(-angle_range,angle_range)
        unit_vector = unit_vector.rotate(angle)
        immigrant_speed = [immigrant_speed_value*unit_vector.x, immigrant_speed_value*unit_vector.y]
        
        immigrant = Invader(immigrant_image, immigrant_position_init, immigrant_speed)
        
        if immigrant.rect.left < horizontal_displacement:
            immigrant.rect.left = horizontal_displacement
        if immigrant.rect.right > screen_width - horizontal_displacement:
            immigrant.rect.right = screen_width - horizontal_displacement

        immigrants.add(immigrant)

    #Generating Drug Dealers 
    if i % dealer_frequency == dealer_frequency -1:
        
        dealer_position_init = random.randint(0,screen_width), 0

        unit_vector = pygame.math.Vector2(0,1)
        angle = random.randint(-angle_range,angle_range)
        unit_vector = unit_vector.rotate(angle)
        dealer_speed = [dealer_speed_value*unit_vector.x, dealer_speed_value*unit_vector.y]
        
        dealer = Invader(dealer_image, dealer_position_init, dealer_speed)

        if dealer.rect.left < horizontal_displacement:
            dealer.rect.left = horizontal_displacement
        if dealer.rect.right > screen_width - horizontal_displacement:
            dealer.rect.right = screen_width - horizontal_displacement
        

        dealers.add(dealer)

    #Generating Trucks of Immigrants 
    if i % truck_frequency == truck_frequency -1:
        truck_position_init = random.randint(0,screen_width), 0
        truck_speed = [0, truck_speed_value]
        truck = Invader(truck_image, truck_position_init, truck_speed)
        
        if truck.rect.left < horizontal_displacement:
            truck.rect.left = horizontal_displacement
        if truck.rect.right > screen_width - horizontal_displacement:
            truck.rect.right = screen_width - horizontal_displacement

        trucks.add(truck)
        
    #----------Deploying chapter2_border Patrol----------#
    deploy_time += 1
    if deploy_time <= deploy_time_limit and deploy_time%deploy_frequency == deploy_frequency-1:
        patrol = Patrol(patrol_image, patrol_position, patrol_speed)
        patrols.add(patrol)

    #Patrols Can't Move when court order is in effect
    for patrol in patrols:
        if court_order_status == 1:
            patrol.speed = [0,0]
        else:
            patrol.speed = patrol_speed

    #----------Declaring National Emergency ---------#
    emergency_time += 1


    wall_position = border_trump.rect.center[0], border_trump.rect.top - 30
    if emergency_time <= emergency_time_limit:
        wall = Wall(wall_long_image, wall_position)
        
    else:
        wall = Wall(wall_short_image, wall_position)



    #----------Collision with Wall or Blocking of Immigrants---------#
    if court_order_status == 0:
        collide_list1 = pygame.sprite.spritecollide(wall, immigrants, False, pygame.sprite.collide_mask)
        for immigrant in collide_list1:
            if immigrant.status == 'legal':
                anger += block_immigrant_anger
            if immigrant.blocked == 0:
                immigrant.speed = [immigrant.speed[0], -immigrant.speed[1]]
                immigrant.blocked = 1
                count += 1
                deploy_charge += 1
                
        
        collide_list2 = pygame.sprite.spritecollide(wall, dealers, False, pygame.sprite.collide_mask)
        for dealer in collide_list2:
            if dealer.blocked == 0:
                dealer.speed = [dealer.speed[0], -dealer.speed[1]]
                dealer.blocked = 1
                count += 1
                deploy_charge += 1

        collide_list3 = pygame.sprite.spritecollide(wall, trucks, False, pygame.sprite.collide_mask)
        for truck in collide_list3:
            if truck.status == 'legal':
                anger += block_truck_anger
            if truck.blocked == 0:
                truck.speed = [truck.speed[0], -truck.speed[1]]
                truck.blocked = 1
                count += 1
                deploy_charge += 1

        #count += len(collide_list1) +len(collide_list2) + len(collide_list3)
        #deploy_charge += len(collide_list1) +len(collide_list2) + len(collide_list3)

        
        if deploy_charge >= patrol_deploy_threshold:
            deploy_charge = patrol_deploy_threshold


    #----------chapter2_border Patrol Arrests Immigrants---------#
    #----------chapter2_border Patrols are Blitted onto the Screen--------#
    for patrol in patrols:
        collide_list4 = pygame.sprite.spritecollide(patrol, immigrants, True, pygame.sprite.collide_mask)
        collide_list5 = pygame.sprite.spritecollide(patrol, dealers, True, pygame.sprite.collide_mask)
        collide_list6 = pygame.sprite.spritecollide(patrol, trucks, True, pygame.sprite.collide_mask)
        count += len(collide_list4) +len(collide_list5) + len(collide_list6)
        patrol.move()
        screen.blit(patrol.image, patrol.rect)


    #----------Announcing Locking Up of Immigrants---------#

    lockup_time += 1

    if lockup_time <= lockup_time_limit and court_order_status == 0: #Can't lock up people when court order is in effect
        
        screen.blit(cage_image, cage_position)
        
        for immigrant in immigrants:

            
            if immigrant.rect.bottom < border_position and immigrant.blocked == 0:
                immigrant.speed = [-immigrant.speed[0], -immigrant.speed[1]]
                immigrant.blocked = 1
            else:
                speed_vector = pygame.math.Vector2(cage_positionx - immigrant.rect.center[0],cage_positiony - immigrant.rect.center[1])
                speed_vector = speed_vector.normalize()
                speed_vector = speed_vector * lockup_speed
                immigrant.speed = [speed_vector.x, speed_vector.y]

            if immigrant.rect.collidepoint(cage_positionx, cage_positiony):
                immigrants.remove(immigrant)
                del immigrant
                count += 1
                
        for truck in trucks:
            if truck.blocked == 0:
                truck.speed = [0, -truck.speed[1]]
                truck.blocked = 1

                
        for dealer in dealers:

            
            if dealer.rect.bottom < border_position and dealer.blocked == 0:
                dealer.speed = [-dealer.speed[0], -dealer.speed[1]]
                dealer.blocked = 1
            else:
                speed_vector = pygame.math.Vector2(cage_positionx - dealer.rect.center[0],cage_positiony - dealer.rect.center[1])
                speed_vector = speed_vector.normalize()
                speed_vector = speed_vector * lockup_speed
                dealer.speed = [speed_vector.x, speed_vector.y]
            if dealer.rect.collidepoint(cage_positionx, cage_positiony):
                dealers.remove(dealer)
                del dealer
                count += 1

    #----------Immigrants and trucks of Immigrants gain Legal Status---------#
    for port in ports:
        for immigrant in immigrants:
            if port.rect.collidepoint(immigrant.rect.center) == True and immigrant.speed[1] > 0:
                immigrant.image = legal_immigrant_image
                immigrant.status = 'legal'
        for truck in trucks:
            if port.rect.collidepoint(truck.rect.center) == True and truck.speed[1] >0:
                truck.image = legal_truck_image
                truck.status = 'legal'
                
                


    #----------Invaders Move---------#
    #----------Invaders are Blitted onto Screen---------#
    #----------Removing Invaders when they Pass Out of Boundaries---------#
    #----------Invaders Damage National Security---------#
    #----------Legal Immigrants and Trucks of Immigrants which are Blocked Cause Anger---------#
                
                
    for immigrant in immigrants:
        immigrant.move()
        screen.blit(immigrant.image, immigrant.rect)

        if immigrant.rect.left < 0 or immigrant.rect.right > screen_width:
            immigrant.speed = [-immigrant.speed[0],immigrant.speed[1]]
            #immigrants.remove(immigrant)
        if immigrant.speed[1] < 0 and immigrant.rect.bottom < 0:
            immigrants.remove(immigrant)
            
        
        if immigrant.rect.top > screen_height:
            if immigrant.status == 'illegal':
                security -= illegal_immigrant_damage
            if immigrant.status == 'legal':
                security -= legal_immigrant_damage
            immigrants.remove(immigrant)
            
        if immigrant.rect.top > screen_height or (immigrant.speed[1] < 0 and immigrant.rect.bottom):
            del immigrant
 

        
    for truck in trucks:
        truck.move()
        screen.blit(truck.image, truck.rect)
        if truck.speed[1] < 0 and truck.rect.bottom < 0:
            trucks.remove(truck)
        if truck.rect.top > screen_height:
            trucks.remove(truck)
            if truck.status == 'illegal':
                security -= illegal_truck_damage
            if truck.status == 'legal':
                security -= legal_truck_damage
        if (truck.speed[1] < 0 and truck.rect.bottom) or truck.rect.top > screen_height:
            del truck

                
    for dealer in dealers:
        dealer.move()
        screen.blit(dealer.image, dealer.rect)
        if dealer.speed[1] < 0 and dealer.rect.bottom < 0:
            dealers.remove(dealer)
        if dealer.rect.left < 0 or dealer.rect.right > screen_width:
            dealer.speed = [-dealer.speed[0],dealer.speed[1]]
            #dealers.remove(dealer)
        if dealer.rect.top > screen_height:
            dealers.remove(dealer)
            security -= dealer_damage
        if (dealer.speed[1] < 0 and dealer.rect.bottom) or dealer.rect.top > screen_height:
            del dealer

    for patrol in patrols:
        if patrol.rect.left > screen_width:
            patrols.remove(patrol)
            del patrol

    if court_order_status == 1:
        for immigrant in immigrants:
            immigrant.speed = [0,immigrant_speed_value]
        for dealer in dealers:
            dealer.speed = [0,dealer_speed]

    #----------Fonts for Ratings---------#
    count_font = pygame.font.Font(None, 30)
    count_text = count_font.render('Immigrants Blocked/Arrested: '+str(count)+'/'+str(count_threshold),True,(255,0,0))
    count_position = (40,20)

    anger_font = pygame.font.Font(None, 30)
    if anger >= anger_warning_threshold:
        anger_text = anger_font.render('Public Discontent: '+str(anger)+'/'+str(anger_threshold),True,(255,0,0))
    else:
        anger_text = anger_font.render('Public Discontent: '+str(anger)+'/'+str(anger_threshold),True,(0,255,0))
    anger_position = (40,50)

    
    security_font = pygame.font.Font(None, 30)
    if security <= security_warning_threshold:
        security_text = security_font.render('National Security Level: '+str(security),True,(255,0,0))
    else:
        security_text = security_font.render('National Security Level: '+str(security),True,(0,255,0))
    security_position = (40,80)

    screen.blit(count_text,count_position)
    screen.blit(anger_text,anger_position)
    screen.blit(security_text,security_position)

    #----------Signs---------#
    
    deploy_charge_font = pygame.font.Font(None, 30)
    deploy_charge_text = deploy_charge_font.render('Patrol Deployment: '+str(deploy_charge)+'/'+str(patrol_deploy_threshold),True,(255,0,0))
    deploy_charge_position = (screen_width - 330,20)

    patrol_ready_font = pygame.font.Font(None, 30)
    patrol_ready_text = patrol_ready_font.render('Ready to Deploy!',True,(255,0,0))
    patrol_ready_position = (screen_width - 330,20)

    if deploy_charge == patrol_deploy_threshold:
        screen.blit(patrol_ready_text, patrol_ready_position)
    else:
        screen.blit(deploy_charge_text, deploy_charge_position)

        
    emergency_charge_font = pygame.font.Font(None, 30)
    emergency_charge_text = emergency_charge_font.render('Emergency Declaration: '+str(emergency_charge)+'/'+str(emergency_frequency_limit),True,(255,0,0))
    emergency_charge_position = (screen_width - 330,50)

    emergency_ready_font = pygame.font.Font(None, 30)
    emergency_ready_text = emergency_ready_font.render('Ready to Declare Emergency!',True,(255,0,0))
    emergency_ready_position = (screen_width - 330,50)

    if emergency_charge >= emergency_frequency_limit:
        screen.blit(emergency_ready_text, emergency_ready_position)
    else:
        screen.blit(emergency_charge_text, emergency_charge_position)

        
    lockup_charge_font = pygame.font.Font(None, 30)
    lockup_charge_text = lockup_charge_font.render('Lockup Preparation: '+str(lockup_charge)+'/'+str(lockup_frequency_limit),True,(255,0,0))
    lockup_charge_position = (screen_width - 330,80)

    lockup_ready_font = pygame.font.Font(None, 30)
    lockup_ready_text = lockup_ready_font.render('Ready to Lock Up Immigrants!',True,(255,0,0))
    lockup_ready_position = (screen_width - 330,80)

    if lockup_charge >= lockup_frequency_limit:
        screen.blit(lockup_ready_text, lockup_ready_position)
    else:
        screen.blit(lockup_charge_text, lockup_charge_position) 

    
    #----------Trump and his Wall Blitted---------#
    screen.blit(border_trump.image, border_trump.rect)
    screen.blit(wall.image, wall.rect)

    if emergency_time <= emergency_time_limit and court_order_status == 0:
        national_emergency_speechbox_position = border_trump.rect.right-80, border_trump.rect.top -60
        screen.blit(national_emergency_speechbox_image,national_emergency_speechbox_position)
        
    if deploy_time <= deploy_time_limit and court_order_status == 0:
        patrol_speechbox_position = border_trump.rect.right-20, border_trump.rect.top -55
        screen.blit(patrol_speechbox_image, patrol_speechbox_position)

    if lockup_time <= lockup_time_limit and court_order_status == 0:
        lockup_speechbox_position = border_trump.rect.right-20, border_trump.rect.top -40
        screen.blit(lockup_speechbox_image, lockup_speechbox_position)
        


    #----------Court Order Sign Blitted---------#
    if court_order_status == 1:
        screen.blit(court_order_image, court_order_position)
        
    
    
    #----------Three Scenarios in which the Game End---------#
    if anger >= anger_threshold:
        lockup_audio.stop()
        emergency_audio.stop()
        patrol_audio.stop()
        protest_audio.play()
        
        screen.fill((255,255,255))
        
        screen.blit(anger_image, (0,0))
        screen.blit(anger_text, anger_text_position)
        screen.blit(anger1_text, anger1_text_position)
        screen.blit(anger2_text, anger2_text_position)

        pygame.display.flip()

        
        pygame.time.delay(cover_time8)
        sys.exit()
        
    if security <= 0:
        lockup_audio.stop()
        emergency_audio.stop()
        patrol_audio.stop()
        
        screen.fill((255,255,255))
        screen.blit(security_image, (0,0))

        screen.blit(security1_text, security1_text_position)
        screen.blit(security2_text, security2_text_position)

        pygame.display.flip()
        riot_audio.play()
        pygame.time.delay(cover_time8)
        sys.exit()   
                
    if count >= count_threshold:
        lockup_audio.stop()
        emergency_audio.stop()
        patrol_audio.stop()
        break
        
    pygame.display.flip()
    screen.fill((255,255,255))

end_chapter2_endscene = False
while not end_chapter2_endscene:
    screen.fill((255,255,255))
    screen.blit(mexico_image, (0,0))
    screen.blit(mexico_text, mexico_text_position)
    screen.blit(mexico1_text, mexico1_text_position)
    screen.blit(mexico2_text, mexico2_text_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter2_endscene = True
                break







end_chapter3_intro1 = False
while not end_chapter3_intro1:
    screen.fill((255,255,255))
    screen.blit(media_war,media_war_position)
    screen.blit(chapter3_text, chapter3_text_position)
    screen.blit(media_war_text,media_war_text_position)  
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter3_intro1 = True
                break

end_chapter3_intro2 = False
while not end_chapter3_intro2:
    screen.fill((255,255,255))
    screen.blit(chapter3,chapter3_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter3_intro2 = True
                break

end_chapter3_intro3 = False
while not end_chapter3_intro3:
    screen.fill((255,255,255))
    screen.blit(instructions3,instructions3_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter3_intro3 = True
                break


#####Chapter 3#####
while True:
    fakenews_audio_charge += 1
    if fakenews_audio_charge >= sound_frequency:
        fakenews_audio_charge = sound_frequency

    
    screen.blit(trump_press1, trump_press1_position)
    i += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            for news_id in list(news_dict.keys()):
                news = news_dict[news_id]
                if news.rect.collidepoint(mouse_position):
                    if fakenews_audio_charge >= sound_frequency:
                        fakenews_audio.play()
                        fakenews_audio_charge = 0
                    
                    news_dict.pop(news_id)
                    news_timeleft_dict.pop(news_id)

                    if news.image == foxnews_image:
                        ratings -= foxnews_add
                    else:
                        points += 1

                    icon = Object(fakenews_image, news.rect.center)
                    icons_dict[news_id] = icon
                    icons_timeleft_dict[news_id] = fakenews_time

        if event.type == pygame.KEYDOWN:
            if clear == 1:
                if event.key == 57:
                    points = 20
                if event.key == 48:
                    ratings = 0
            
            

            
    for chair in chairs:
        screen.blit(chair.image, chair.rect)

    if i%frequency1 == frequency1 -1:
        k += 1
        news_image = random.choice(media_images)
        news_position = random.choice(news_positions)
        news = Object(news_image, news_position)
        news_list.append(news)

        news_id = k
        news_timeleft_dict[news_id] = news_time
        news_dict[news_id] = news
        
    for news_id in news_timeleft_dict.keys():
        news_timeleft_dict[news_id] -= 1

    for icon_id in icons_timeleft_dict.keys():
        icons_timeleft_dict[icon_id] -= 1

    #news_timeleft_dict_keys = news_timeleft_dict.keys()

    news_timeleft_dict_keys = list(news_timeleft_dict.keys())
    for news_id in news_timeleft_dict_keys:

        if news_timeleft_dict[news_id] <= 0:
            news = news_dict[news_id]
            if news.image == foxnews_image:
                ratings += foxnews_add
            else:            
                ratings -= fakenews_damage
            try:
                news_timeleft_dict.pop(news_id)
            except:
                pass

            try:
                news_dict.pop(news_id)
            except:
                pass
            news_timeleft_dict_keys = list(news_timeleft_dict.keys())

    for icon_id in list(icons_timeleft_dict.keys()):
        
        if icons_timeleft_dict[icon_id] <= 0:
            try:
                icons_timeleft_dict.pop(icon_id)
            except:
                pass

            try:
                icons_dict.pop(icon_id)
            except:
                pass
                
                
    
    for news in news_dict.values():
        screen.blit(news.image, news.rect)
    for icon in icons_dict.values():
        screen.blit(icon.image, icon.rect)

    points_font = pygame.font.Font(None,60)
    points_text = points_font.render('Points: '+str(points)+'/'+str(points_threshold),True,(255,0,0))
    screen.blit(points_text,(50,50))

    ratings_font = pygame.font.Font(None,60)
    ratings_text = ratings_font.render('Ratings: '+str(ratings)+'%',True,(255,0,0))
    screen.blit(ratings_text,(screen_width-275,50))

    if ratings <= 0:
        winning = 0
        impeached_audio.play()

        break

    if points == points_threshold:
        winning = 1
        impeached_audio.play()
        break

    pygame.display.flip()
    screen.fill((0,0,255))
        
        
if winning == 0:
    end_chapter3_endscene1 = False
    while not end_chapter3_endscene1:
        screen.fill((255,255,255))
        screen.blit(impeach,impeach_position)
        screen.blit(lost_text, lost_text_position)
        screen.blit(lost2_text, lost2_text_position)
        screen.blit(button_image, button_position)
        pygame.display.flip()
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                if button_position.collidepoint(mouse_position):
                    end_chapter3_endscene1 = True
                    impeached_audio.fadeout(fadeout_time)
                    break
if winning == 1:
    end_chapter3_endscene2 = False
    while not end_chapter3_endscene2:
        screen.fill((255,255,255))
        screen.blit(impeach,impeach_position)
        screen.blit(won_text, won_text_position)
        screen.blit(won2_text, won2_text_position)
        screen.blit(button_image, button_position)
        pygame.display.flip()
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                if button_position.collidepoint(mouse_position):
                    end_chapter3_endscene2 = True
                    impeached_audio.fadeout(fadeout_time)
                    impeached_audio.stop()
                    break    



class Senator(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.rect.bottom = position[1]
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
    def move2(self, speed):
        self.rect = self.rect.move(speed)

senator_images = [bernie_image, chuck_image, cory_image , kamala_image , warren_image , nancy_image , mitch_image , ted_image]





senators = []
senators_dict = {}




stop_audio_charge = 0
index = 0
impeachment_progress = 0
term_progress = 0
i = 0


end_chapter4_intro1 = False
while not end_chapter4_intro1:
    screen.fill((255,255,255))
    screen.blit(trial,(0,0))
    screen.blit(chapter4_text, chapter4_text_position)
    screen.blit(impeachment_saga_text,impeachment_saga_text_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter4_intro1 = True
                break

end_chapter4_intro2 = False
while not end_chapter4_intro2:
    screen.fill((255,255,255))
    screen.blit(trial,(0,0))
    screen.blit(chapter4,chapter4_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter4_intro2 = True
                break

end_chapter4_intro3 = False
while not end_chapter4_intro3:
    screen.fill((255,255,255))
    screen.blit(trial,(0,0))
    screen.blit(instructions4,instructions4_position)
    screen.blit(button_image, button_position)
    pygame.display.flip()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if button_position.collidepoint(mouse_position):
                end_chapter4_intro3 = True
                break
            
while True:
    stop_audio_charge += 1
    if stop_audio_charge >= sound_frequency:
        stop_audio_charge = sound_frequency
        
    i += 1
    screen.blit(congress,(0,0))

    term_progress += term_speed
    trump_speed = [0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == 97:
                trump_speed = [-screen_width/6,0]
            if event.key == 100:
                trump_speed = [screen_width/6,0]
                
            if clear == 1:
                if event.key == 57:
                    term_progress = 4*365
                if event.key == 48:
                    impeachment_progress = 100
                
    if i % frequency == frequency-1:
        senator_image = random.choice(senator_images)
        speeds_copy = speeds[:]
        del speeds_copy[index]
        
        senator_speed = random.choice(speeds_copy)
        index = speeds.index(senator_speed)

        senator_position = (screen_width/2, displacement)
        senator = Senator(senator_image, senator_position, senator_speed)
        senators_dict[i] = senator
       

    for senator_id in list(senators_dict.keys()):
        senatorx = senators_dict[senator_id]

        senatorx.move()
        screen.blit(senatorx.image,senatorx.rect)
        
    for senator_id in list(senators_dict.keys()):
        senator = senators_dict[senator_id]
        if senator.rect.top > screen_height and senator.speed[1] > 0:
            if senator.image == bernie_image:
                impeachment_progress += 9
            if senator.image == chuck_image:
                impeachment_progress += 15
            if senator.image == cory_image:
                impeachment_progress += 4
            if senator.image == kamala_image:
                impeachment_progress += 4
            if senator.image == warren_image:
                impeachment_progress += 8
            if senator.image == mitch_image:
                pass
                
            if senator.image == ted_image:
                pass   
            senators_dict.pop(senator_id)
            
        if senator.rect.bottom < displacement and senator.speed[1] < 0:    
            senators_dict.pop(senator_id)
        

            
    trump3_position = trump3_position.move(trump_speed)
    
    if trump3_position.left<0:
        trump3_position.center = screen_width/6, screen_height
        trump3_position.bottom = screen_height
    if trump3_position.right>screen_width:
        trump3_position.center = screen_width*5/6, screen_height
        trump3_position.bottom = screen_height
    
    screen.blit(trump3,trump3_position)
    senator_id_list = list(senators_dict.keys())

    for senator_id in senator_id_list:
        senatorx = senators_dict[senator_id]
        if senatorx.speed[1] < 0:
            continue
        if trump3_position.colliderect(senatorx.rect) == True:

            senatorx.speed = [-senatorx.speed[0],-senatorx.speed[1]]
            if stop_audio_charge >= sound_frequency:
                stop_audio.play()
                stop_audio_charge = 0


    term_years = int(term_progress/365)
    term_days = int(term_progress - term_years * 365)
       

    impeachment_progress_font = pygame.font.Font(None,40)
    impeachment_progress_text = impeachment_progress_font.render('chapter4_impeachment progress: '+str(impeachment_progress)+'%',True,(0,0,255))
    if impeachment_progress > 85:
        impeachment_progress_text = impeachment_progress_font.render('chapter4_impeachment progress: '+str(impeachment_progress)+'%',True,(255,0,0))
    screen.blit(impeachment_progress_text,(50,50))

    term_progress_font = pygame.font.Font(None,40)
    term_progress_text = term_progress_font.render('term progress: '+str(term_years)+' years '+str(term_days)+' days',True,(255,0,0))
    screen.blit(term_progress_text,(screen_width-450,50))

    if term_years == term_limit or impeachment_progress >= 100:
        if term_years == term_limit:

            screen.blit(retired,(0,0))


            screen.blit(avoided_text, avoided_text_position)
            screen.blit(retired_text, retired_text_position)
        else:
            

            screen.blit(impeached,(0,0))

            screen.blit(impeached_text, impeached_text_position)
            screen.blit(removed_text, removed_text_position)        

        game_over_font = pygame.font.Font(None,60)
        game_over_text = game_over_font.render('GAME OVER!',True,(0,0,255))
        game_over_text_position = game_over_text.get_rect()
        game_over_text_position.center = screen_width/2, screen_height/2 + 50
        screen.blit(game_over_text, game_over_text_position)

        pygame.display.flip()
        sys.exit()

    pygame.display.flip()
    screen.fill((255,255,255))


