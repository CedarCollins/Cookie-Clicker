import pygame
pygame.init()

class Button():
    def __init__(self, x, y, image, scale = 1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def click(self):
        action = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

def show_count(x, y, color, font, text, value = ''):
    score = font.render(text + str(value), True, color)
    screen.blit(score, (x, y))
    
def price(upgrade, n):
    if upgrade == 'mouse_upgrade':
        return (5000*(10**n))
    if upgrade == 'autoclicker':
        return (5 + 5*n)
    if upgrade == 'grandma':
        return (50 + 50*n)
    if upgrade == 'farm':
        return (500 + 500*n)
    if upgrade == 'mine':
        return (5000 + 5000*n)
    if upgrade == 'factory':
        return (50000 + 50000*n)
    if upgrade == 'bank':
        return (500000 + 500000*n)
    if upgrade == 'shipment':
        return (5000000 + 5000000*n)

def main():
    #color library

    black = (0, 0, 0)
    dark_gray = (40, 40, 40)
    white = (255, 255, 255)

    #create display window
    global screen
    screen = pygame.display.set_mode((700,600))
    pygame.display.set_caption('Cookie Clicker Remake')
    framerate = 30
    cookie_font = pygame.font.Font('freesansbold.ttf', 40)
    upgrade_font = pygame.font.Font('freesansbold.ttf', 14)
    cps_font = pygame.font.Font('freesansbold.ttf',22)
    timer = pygame.time.Clock()

    #load images
    background_img = pygame.image.load('Images/background.png').convert_alpha()
    cookie_img = pygame.image.load('Images/cookie.png').convert_alpha()
    mouse_upgrade_img = pygame.image.load('Images/mouse_upgrade.png').convert_alpha()
    autoclicker_img = pygame.image.load('Images/autoclicker.png').convert_alpha()
    grandma_img = pygame.image.load('Images/grandma.png').convert_alpha()
    farm_img = pygame.image.load('Images/farm.png').convert_alpha()
    mine_img = pygame.image.load('Images/mine.png').convert_alpha()
    factory_img = pygame.image.load('Images/factory.png').convert_alpha()
    bank_img = pygame.image.load('Images/bank.png').convert_alpha()
    shipment_img = pygame.image.load('Images/shipment.png').convert_alpha()
    
    #create button instances
    cookie = Button(95, 195, cookie_img, 0.8)
    mouse_upgrade = Button(450, 0, mouse_upgrade_img)
    autoclicker = Button(450, 75, autoclicker_img)
    grandma = Button(450, 150, grandma_img)
    farm = Button(450, 225, farm_img)
    mine = Button(450, 300, mine_img)
    factory = Button(450, 375, factory_img)
    bank = Button(450, 450, bank_img)
    shipment = Button(450, 525, shipment_img)

    #Initialize variables
    try:
        infile = open('data.txt','r')
        
        cookie_total = int(infile.readline())

        mouse_upgrade_total = int(infile.readline())
        autoclicker_total = int(infile.readline())
        grandma_total = int(infile.readline())
        farm_total = int(infile.readline())
        mine_total = int(infile.readline())
        factory_total = int(infile.readline())
        bank_total = int(infile.readline())
        shipment_total = int(infile.readline())

        click_scalar = int(infile.readline())
        autoclicker_amount = int(infile.readline())
        grandma_amount = int(infile.readline())
        farm_amount = int(infile.readline())
        mine_amount = int(infile.readline())
        factory_amount = int(infile.readline())
        bank_amount = int(infile.readline())
        shipment_amount = int(infile.readline())
        
        infile.close()

    except: 
        cookie_total = 0

        mouse_upgrade_total = 0
        autoclicker_total = 0
        grandma_total = 0
        farm_total = 0
        mine_total = 0
        factory_total = 0
        bank_total = 0
        shipment_total = 0

        click_scalar = 1
        autoclicker_amount = 0
        grandma_amount = 0
        farm_amount = 0
        mine_amount = 0
        factory_amount = 0
        bank_amount = 0
        shipment_amount = 0

    time = 0
    counter = 0

    #game loop
    running = True
    while running:
        
        screen.blit(background_img, (0,0))

        #triggers for actions when buttons are clicked
        if cookie.click():
            cookie_total += 1*click_scalar

        if mouse_upgrade.click():
            if cookie_total >= price('mouse_upgrade', mouse_upgrade_total):
                cookie_total -= price('mouse_upgrade', mouse_upgrade_total)
                mouse_upgrade_total += 1
                click_scalar = 10**mouse_upgrade_total
        
        if autoclicker.click():
            if cookie_total >= price('autoclicker', autoclicker_total):
                cookie_total -= price('autoclicker', autoclicker_total)
                autoclicker_total += 1
                autoclicker_amount += 1
        
        if grandma.click():
            if cookie_total >= price('grandma', grandma_total):
                cookie_total -= price('grandma', grandma_total)
                grandma_total += 1
                grandma_amount += 1
        
        if farm.click():
            if cookie_total >= price('farm', farm_total):
                cookie_total -= price('farm', farm_total)
                farm_total += 1
                farm_amount += 10

        if mine.click():
            if cookie_total >= price('mine', mine_total):
                cookie_total -= price('mine', mine_total)
                mine_total += 1
                mine_amount += 100

        if factory.click():
            if cookie_total >= price('factory', factory_total):
                cookie_total -= price('factory', factory_total)
                factory_total += 1
                factory_amount += 1000

        if bank.click():
            if cookie_total >= price('bank', bank_total):
                cookie_total -= price('bank', bank_total)
                bank_total += 1
                bank_amount += 10000

        if shipment.click():
            if cookie_total >= price('shipment', shipment_total):
                cookie_total -= price('shipment', shipment_total)
                shipment_total += 1
                shipment_amount += 100000

        #timer for everything else
        now = pygame.time.get_ticks()
        if now > (time + 1000):
            cookie_total += grandma_amount + farm_amount + mine_amount + factory_amount + bank_amount + shipment_amount
            time = now
            counter += 1
            if counter == 10:
                counter = 0
                cookie_total += autoclicker_amount

        #update counters
        show_count(5, 5, black, cookie_font, "Cookies: ", cookie_total)
        show_count(510, 10, black, upgrade_font, "Mouse Upgrades ", mouse_upgrade_total)
        show_count(510, 85, black, upgrade_font, "Autoclickers ", autoclicker_total)
        show_count(510, 160, black, upgrade_font, "Grandmas ", grandma_total)
        show_count(510, 235, black, upgrade_font, "Farms ", farm_total)
        show_count(510, 310, black, upgrade_font, "Mines ", mine_total)
        show_count(510, 385, black, upgrade_font, "Factories ", factory_total)
        show_count(510, 460, black, upgrade_font, "Banks ", bank_total)
        show_count(510, 535, black, upgrade_font, "Shipments ", shipment_total)

        #update prices
        show_count(510, 30, black, upgrade_font, "Price ", price('mouse_upgrade', mouse_upgrade_total))
        show_count(510, 105, black, upgrade_font, "Price ", price('autoclicker', autoclicker_total))
        show_count(510, 180, black, upgrade_font, "Price ", price('grandma', grandma_total))
        show_count(510, 255, black, upgrade_font, "Price ", price('farm', farm_total))
        show_count(510, 330, black, upgrade_font, "Price ", price('mine', mine_total))
        show_count(510, 405, black, upgrade_font, "Price ", price('factory', factory_total))
        show_count(510, 480, black, upgrade_font, "Price ", price('bank', bank_total))
        show_count(510, 555, black, upgrade_font, "Price ", price('shipment', shipment_total))

        #upgrade increase
        show_count(510, 50, black, upgrade_font, "Adds 10x Cookies per Click")
        show_count(510, 125, black, upgrade_font, "Each Adds 0.1 CPS")
        show_count(510, 200, black, upgrade_font, "Each Adds 1 CPS")
        show_count(510, 275, black, upgrade_font, "Each Adds 10 CPS")
        show_count(510, 350, black, upgrade_font, "Each Adds 100 CPS")
        show_count(510, 425, black, upgrade_font, "Each Adds 1,000 CPS")
        show_count(510, 500, black, upgrade_font, "Each Adds 10,000 CPS")
        show_count(510, 575, black, upgrade_font, "Each Adds 100,000 CPS")

        cps = round(0.1*autoclicker_total, 1) + grandma_total + 10*farm_total + 100*mine_total + 1000*factory_total + 10000*bank_total + 100000*shipment_total
        show_count(5, 45, black, cps_font, "Cookies per Second (CPS): ", cps)
        
        timer.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    outfile = open('data.txt','w')
    variables_list = [cookie_total, mouse_upgrade_total, autoclicker_total, grandma_total, farm_total, mine_total, factory_total, bank_total, shipment_total, click_scalar, autoclicker_amount, grandma_amount, farm_amount, mine_amount, factory_amount, bank_amount, shipment_amount]
    for item in variables_list:
        outfile.write(str(item) + '\n')
    outfile.close()

    pygame.quit()

if __name__ == '__main__':
    main()
