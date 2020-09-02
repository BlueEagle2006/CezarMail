# -*- coding: cp1254 -*-
import pygame;
import random,time,keyboard,datetime;
pygame.init();
gd = pygame.display.set_mode((900,700))
pygame.display.set_caption('Cezar Mail');
logo = pygame.image.load('Cmail Logo.png')
login = pygame.image.load('Login1.png')
loginB = pygame.image.load('Login2.png')
sign = pygame.image.load('Sign.png')
Page = pygame.image.load('Sayfa.png')
New = pygame.image.load('Mesaj.png')
box = pygame.image.load('Posta.png')
def text_objects(text,font,renk):
    textS=font.render(text,True,renk)
    return(textS)
def pprint(text,x,y,renk):
    LT = pygame.font.Font('freesansbold.ttf',15);
    Text = text_objects(text,LT,renk)
    gd.blit(Text,(x,y))
    pygame.display.update();
def Oyun_Snake():
    def score(number):
        font = pygame.font.SysFont(None,30);
        text = font.render('Apples: '+str(number),True,(255,255,255))
        gd.blit(text,(0,0));
    def snake(x,y,ax,ay,sp):
        pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
        pygame.draw.rect(gd,(255,0,0),[(ax*40),(ay*40),40,40]);
        pygame.draw.rect(gd,(255,255,0),[x,y,40,40]);
        for i in range(len(sp)):
            if i%2==0:
                pygame.draw.rect(gd,(255,255,0),[(sp[i]),(sp[i+1]),40,40]);
    def text_objects(text,font):
        textS=font.render(text,True,(255,255,255))
        return(textS)
    def pprint(text):
        LT = pygame.font.Font('freesansbold.ttf',40);
        Text = text_objects(text,LT)
        gd.blit(Text,(180,80))
        pygame.display.update();
    def game_loop():
        while True:
            sayi=0;
            x = 200;
            y = 240;
            b=1;
            xC=0;
            yC=0;
            sxC=0;
            syC=0;
            ax=11;
            ay=6;
            Dur=0;
            gd.fill((255,255,255));
            pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
            pprint('Snake Game');
            time.sleep(1);
            pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
            pprint('by Can ER')
            time.sleep(1);
            sp=[160,240,120,240]
            Q = False;
            while not Q:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Dur=1;
                if Dur==1:
                    break;
                snake(x,y,ax,ay,sp);
                score(sayi);
                pygame.display.update();
                key = pygame.key.get_pressed();
                if x==(ax*40) and y==(ay*40):
                    sayi+=1                
                    sp.append(sp[(len(sp)-1)-1])
                    sp.append(sp[(len(sp)-1)-3])
                    while True:
                        o=0;
                        ax=random.randrange(0,15)
                        ay=random.randrange(0,15)
                        for i in range(len(sp)):
                            if i%2==0:
                                if sp[i]==(ax*40) and sp[i+1]==(ay*40):
                                    o=1;
                                if x==(ax*40) and y==(ay*40):
                                    o=1;
                        if o==0:
                            break;
                if key[pygame.K_RIGHT] or key[pygame.K_d]:
                    if (xC)!=(-40):
                        xC=40;
                        yC=0;
                        time.sleep(0.001);
                        b=0;
                if key[pygame.K_LEFT] or key[pygame.K_a]:
                    if (xC)!=(40)and b==0:
                        xC=-40;
                        yC=0;
                        time.sleep(0.001);
                if key[pygame.K_UP] or key[pygame.K_w]:
                    if (yC)!=(40):
                        xC=0;
                        yC=-40;
                        time.sleep(0.001);
                        b=0;
                if key[pygame.K_DOWN] or key[pygame.K_s]:
                    if (yC)!=(-40):
                        xC=0;
                        yC=40;
                        time.sleep(0.001);
                        b=0;
                if b==0:
                    for i in range(len(sp)-1,-1,-1):
                        if i>=2 and i%2==0:
                            sp[i]=sp[i-2]
                            sp[i+1]=sp[i-1]
                    sp[0]=x;
                    sp[1]=y;
                x=x+xC;
                y=y+yC;
                p=0;
                for i in range(len(sp)):
                    if i%2==0:
                        if sp[i]==x and sp[i+1]==y:
                            p+=1;
                            break;
                if p==1:
                    time.sleep(1);
                    Q = True;
                if x<0:
                    x=560;
                if x>560:
                    x=0;
                if y<0:
                    y=560;
                if y>560:
                    y=0;
                time.sleep(0.13);
                pygame.display.update();
            if Dur==1:
                break;
    game_loop();
def Oyun_Pong():
    def score(number1,number2):
        font = pygame.font.SysFont(None,40);
        text = font.render(str(number1),True,(255,255,255))
        gd.blit(text,(200,0));
        text = font.render(str(number2),True,(255,255,255))
        gd.blit(text,(400,0));
    def pong(x1,y1,x2,y2,bx,by):
        pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1-10),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1-20),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1-30),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1-40),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1-50),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x1),(y1-60),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2-10),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2-20),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2-30),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2-40),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2-50),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(x2),(y2-60),10,10]);
        pygame.draw.rect(gd,(255,255,255),[(bx),(by),10,10]);
    def text_objects(text,font):
        textS=font.render(text,True,(255,255,255))
        return(textS)
    def pprint(text):
        LT = pygame.font.Font('freesansbold.ttf',40);
        Text = text_objects(text,LT)
        gd.blit(Text,(180,80))
        pygame.display.update();
    def game_loop():
        while True:
            pause=1;
            robo=0;
            sayi1=0;
            sayi2=0;
            x1 = 20;
            y1 = 330;
            x2 = 570;
            y2 = 330;
            bx = 290
            by = 290
            yonx=1;
            yony=1;
            Dur=0;
            gd.fill((255,255,255))
            pygame.display.update();
            pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
            pprint('Pong');
            time.sleep(1);
            pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
            pprint('by Can ER')
            time.sleep(1);
            Q = False;
            while not Q:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Dur=1;
                if Dur==1:
                    break;
                pong(x1,y1,x2,y2,bx,by);
                score(sayi1,sayi2);
                pygame.display.update();
                key = pygame.key.get_pressed();
                if key[pygame.K_UP]:
                    if (y2-10)>=50:
                        y2=y2-10;
                        pause=0;
                    time.sleep(0.001);
                if key[pygame.K_DOWN]:
                    if (y2+10)<=590:
                        y2=y2+10;
                        pause=0;
                    time.sleep(0.001);
                if robo==0:
                    if key[pygame.K_w]:
                        if (y1-10)>=50:
                            y1=y1-10;
                            pause=0;
                        time.sleep(0.001);
                    if key[pygame.K_s]:
                        if (y1+10)<=590:
                            y1=y1+10;
                            pause=0;
                        time.sleep(0.001);
                else:
                    if (y1-30)>by:
                        if (y1-10)>=50:
                            y1=y1-10;
                            pause=0;
                        time.sleep(0.001);
                    if (y1-30)<by:
                        if (y1+10)<=590:
                            y1=y1+10;
                            pause=0;
                        time.sleep(0.001);
                if pause==0:
                    if bx>=590:
                        sayi1+=1;
                        time.sleep(1);
                        bx = 290
                        by = 290
                        yonx=1;
                        yony=1;
                        x1 = 20;
                        y1 = 330;
                        x2 = 570;
                        y2 = 330;
                    if bx<=0:
                        sayi2+=1;
                        time.sleep(1);
                        bx = 290
                        by = 290
                        yonx=2;
                        yony=2;
                        x1 = 20;
                        y1 = 330;
                        x2 = 570;
                        y2 = 330;
                    if by>=590:
                        yony=2
                    if by<=0:
                        yony=1
                    if yony==1:
                        by=by+6;
                    if yony==2:
                        by=by-6;
                    if (by<=y1 and by>=(y1-60)) and bx<=20:
                        yonx=2
                    if (by<=y2 and by>=(y2-60)) and bx>=570:
                        yonx=1
                    if yonx==1:
                        bx=bx-10;
                    if yonx==2:
                        bx=bx+10;
                    if key[pygame.K_1]:
                        robo=0;
                        pause=0;
                    if key[pygame.K_2]:
                        robo=1;
                        pause=0;
                    if key[pygame.K_0]:
                        break;
                    pygame.display.update();
                    time.sleep(0.025);
            if Dur==1:
                break;
    game_loop();
def gmail_posts():
    return 0;
def sifrele(x,sifre,r):
    s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.',',','?','!','(',')',':','/','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i']
    sayi=[]
    d=(random.randrange(1,10));
    ss=[];
    for j in range(len(sifre)):
        for i in range(len(s)-9):
            if sifre[j]==s[i]:
                sayi.append(i);
    for i in range(len(sifre)):
        ss.append(s[(sayi[i]+d)]);
    z=''
    for i in range(len(ss)):
        z=(z+ss[i])
    z30=True;
    while z30==True:
        if r=='CezarMail':
            v0=open('Cezar Mail Kisiler\\Admin.txt','a');
            k=datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            v0.write('from:'+str(x)+'@Cmail.com\n'+str(z)+'\n'+str(d)+'\n'+str(k)+'\n');
            v0.close();
            break;
        else:
            try:
                v=open('Cezar Mail Kisiler\\'+str(r)+'.txt','r');
                v.close();
                v0=open('Cezar Mail Kisiler\\'+str(r)+'.txt','a');
                k=datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                v0.write('from:'+str(x)+'@Cmail.com\n'+str(z)+'\n'+str(d)+'\n'+str(k)+'\n');
                v0.close();
                break;
            except:
                pprint('There is no User Name named in this name',150,10,(255,0,0));
                break;
def coz(un1,p1,PostaNumara):
    du=0;
    s=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','.',',','?','!','(',')',':','/','0','1','2','3','4','5','6','7','8','9']
    while True:
        mouse = pygame.mouse.get_pos();
        click = pygame.mouse.get_pressed();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit();
        if un1=='CezarMail':
            v1=open('Cezar Mail Kisiler\\Admin.txt','r');
        else:
            v1=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','r');
        while True:
            try:        
                v2=v1.read()
                f=v1.readlines(2);
                x=(v2[len(un1)+len(p1)+1:]);
                x=x.split('\n');
                fr=str(x[(PostaNumara*4)+1][5:])
                ss=str(x[(PostaNumara*4)+2])
                d=int(x[(PostaNumara*4)+3])
                gt=str(x[(PostaNumara*4)+4]);
                v1.close();
                break;
            except:
                a=1
        sayi=[];
        ssc=[];
        for j in range(len(ss)+9):
            if j >=9:
                for i in range(len(s)):
                    if ss[j-9]==s[i] and i>=9:
                         sayi.append(i);
        for i in range(len(ss)):
            ssc.append(s[(sayi[i]-d)]);
        z=''
        for i in range(len(ssc)):
            z=(z+ssc[i])
        if du==0:
            gd.fill((255,255,255));
            gd.blit(logo,(10,10));
            gd.blit(Page,(10,100));
            pygame.display.update();
            pprint('Welcome '+str(un1),700,130,(0,0,0));
            for j in range(int(len(z)/70)+1):
                pprint(str(z[(70*j):70+(70*j)]),180,250+(j*15),(0,0,0));
            pprint('From:'+str(fr),175,180,(0,0,0))
            pprint('Sending Date:'+str(gt),550,180,(0,0,0))
            pprint('Exit',15,180,(0,0,0))
            pprint('Delete',15,205,(0,0,0))
            du=1;
        if (((10<mouse[0]<145) and (102<mouse[1]<170)) or ((160<mouse[0]<285) and (113<mouse[1]<165)) or ((14<mouse[0]<150) and (175<mouse[1]<195))) and (click[0]==1):
            break;
        if ((14<mouse[0]<150) and (195<mouse[1]<215)) and (click[0]==1):
            if un1=='CezarMail':
                v2=open('Cezar Mail Kisiler\\Admin.txt','r');
            else:
                v2=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','r');
                v0=v2.read()
                x=(v0[int(len(un1)+len(p1)+2):]);
                x=x.split('\n');
                y=[];
                cs=str(x[(PostaNumara*4)+1]);
                number=str(x[(PostaNumara*4)+2]);
                gt=str(x[(PostaNumara*4)+3]);
                for i in range(len(x)):
                    if int(i+1)%4==0 and (str(gt)!=str(x[i]) or str(number)!=str(x[i-1]) or str(cs)!=str(x[i-2])):            
                        y.append(str(x[int(i-3)])+'\n');
                        y.append(str(x[int(i-2)])+'\n');
                        y.append(str(x[int(i-1)])+'\n');
                        y.append(str(x[int(i)])+'\n');
                q='';
                for i in range(len(y)):
                    q=q+str(y[i]);
                v1.close();
                if un1=='CezarMail':
                    f0=open('Cezar Mail Kisiler\\Admin.txt','w');
                else:
                    f0=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','w');
                f0.truncate(0);
                f0.write(str(un1)+'\n'+str(p1)+'\n');
                if (int(len(q)) >= 10):
                    f0.write(str(q));
                f0.close();
                break;
def Postalar(un1,p1):
    du=0;
    while True:
        mouse = pygame.mouse.get_pos();
        click = pygame.mouse.get_pressed();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit();
        if un1=='CezarMail':
            v1=open('Cezar Mail Kisiler\\Admin.txt','r');
        else:
            v1=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','r');
        v2=v1.read()
        posts=(v2[len(un1)+len(p1)+2:]);
        posts=posts.split('\n')
        v1.close();
        if du==0:
            pprint('Exit',15,180,(0,0,0))
        if len(posts)<=2:   
            pprint('You Have No Post.',300,200,(0,0,0));
            break;
        else:
            if du==0:
                b=0;
                gd.fill((200,200,200));
                gd.blit(logo,(10,10));
                gd.blit(Page,(10,100));
                pygame.display.update();
                pprint('Welcome '+str(un1),700,130,(0,0,0));
                pprint('Exit',15,180,(0,0,0))
                for i in range((len(posts)-1)/4):
                    gd.blit(box,(170,170+(b*56)))
                    pprint(str(posts[(i*4)]),180,175+(b*56),(0,0,0));
                    pprint(str(posts[1+(i*4)][:20]),200,190+(b*56),(0,0,0));
                    pprint(str(posts[3+(i*4)]),500,200+(b*56),(0,0,0));
                    du=1;
                    b+=1;
                    pygame.display.update();
            if (170<mouse[0]<670) and (170<mouse[1]) and (click[0]==1):
                if (170<mouse[1]<226):
                    coz(un1,p1,0);
                if (226<mouse[1]<282):
                    coz(un1,p1,1);
                if (282<mouse[1]<338):
                    coz(un1,p1,2);
                if (338<mouse[1]<394):
                    coz(un1,p1,3);
                if (394<mouse[1]<450):
                    coz(un1,p1,4);
                if (450<mouse[1]<506):
                    coz(un1,p1,5);
                if (506<mouse[1]<562):
                    coz(un1,p1,6);
                if (562<mouse[1]<618):
                    coz(un1,p1,7);
                if (618<mouse[1]<674):
                    coz(un1,p1,8);
                time.sleep(0.1);
                du=0;
            if (((10<mouse[0]<145) and (102<mouse[1]<170)) or ((160<mouse[0]<285) and (113<mouse[1]<165)) or ((14<mouse[0]<150) and (175<mouse[1]<195))) and (click[0]==1):
                break;
        time.sleep(0.01);
def CezarMail_loop():
    un1='';
    p1='';
    p2='';
    alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','?']
    alf2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','!','"','^','+','%','&','/','(',')']
    Q = False;
    while not Q:
        mouse = pygame.mouse.get_pos();
        click = pygame.mouse.get_pressed();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                exit();
        key = pygame.key.get_pressed();
        gd.fill((255,255,255))
        if (400<mouse[0]<477) and (448<mouse[1]<485):
            gd.blit(loginB,(300,200))
            if (click[0]==1):
                un1='';
                p1='';
                while True:
                    mouse = pygame.mouse.get_pos();
                    click = pygame.mouse.get_pressed();
                    gd.fill((255,255,255))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit();
                            exit();
                    gd.blit(sign,(300,200))
                    if (350<mouse[0]<535) and (305<mouse[1]<340) and (click[0]==1):
                        pprint(str(un1),350,315,(0,0,0));
                        pprint(str(p1),350,375,(0,0,0));
                        pprint(str(p2),350,425,(0,0,0));
                        while not keyboard.is_pressed('Enter'):
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit();
                                    exit();
                            for i in range(len(alf)):
                                if keyboard.is_pressed('backspace'):
                                    un1=un1[:(len(un1)-1)];
                                    gd.fill((255,255,255))
                                    gd.blit(sign,(300,200))
                                    pygame.display.update();
                                    pprint(str(un1),350,315,(0,0,0));   
                                    time.sleep(0.12);
                                if keyboard.is_pressed('space'):
                                    un1=un1+' ';
                                    pprint(str(un1),350,315,(0,0,0));   
                                    time.sleep(0.12);
                                elif keyboard.is_pressed('shift+'+str(alf[i])) and len(un1)<20:
                                    un1=un1+str(alf2[i])
                                    time.sleep(0.12);
                                    pprint(str(un1),350,315,(0,0,0));
                                elif keyboard.is_pressed(str(alf[i])) and len(un1)<20:
                                    un1=un1+str(alf[i]);
                                    time.sleep(0.12);
                                    pprint(str(un1),350,315,(0,0,0));
                    else:
                        if un1=='':
                            pprint('User Name:',350,315,(0,0,0))
                        else:
                            pprint(str(un1),350,315,(0,0,0));
                    if (350<mouse[0]<535) and (365<mouse[1]<400) and (click[0]==1):
                        pprint(str(un1),350,315,(0,0,0));
                        pprint(str(p1),350,375,(0,0,0));
                        pprint(str(p2),350,425,(0,0,0));
                        while not keyboard.is_pressed('Enter'):
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit();
                                    exit();
                            for i in range(len(alf)):
                                if keyboard.is_pressed('backspace'):
                                    p1=p1[:(len(p1)-1)];
                                    gd.fill((255,255,255))
                                    gd.blit(sign,(300,200))
                                    pygame.display.update();
                                    pprint(str(p1),350,375,(0,0,0));   
                                    time.sleep(0.1);
                                if keyboard.is_pressed('space'):
                                    p1=p1+' '
                                    pprint(str(p1),350,375,(0,0,0));   
                                    time.sleep(0.1);  
                                elif keyboard.is_pressed('shift+'+str(alf[i])) and len(p1)<20:
                                    p1=p1+str(alf2[i])
                                    time.sleep(0.1);
                                    pprint(str(p1),350,375,(0,0,0));
                                elif keyboard.is_pressed(str(alf[i])) and len(p1)<20:
                                    p1=p1+str(alf[i]);
                                    time.sleep(0.1);
                                    pprint(str(p1),350,375,(0,0,0));
                    else:
                        if p1=='':
                            pprint('Password:',350,375,(0,0,0))
                        else:
                            pprint(str(p1),350,375,(0,0,0));
                    if (350<mouse[0]<535) and (414<mouse[1]<450) and (click[0]==1):
                        pprint(str(un1),350,315,(0,0,0));
                        pprint(str(p1),350,375,(0,0,0));
                        pprint(str(p2),350,425,(0,0,0));
                        while not keyboard.is_pressed('Enter'):
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit();
                                    exit();
                            for i in range(len(alf)):
                                if keyboard.is_pressed('backspace'):
                                    p2=p2[:(len(p2)-1)];
                                    gd.fill((255,255,255))
                                    gd.blit(sign,(300,200))
                                    pygame.display.update();
                                    pprint(str(p2),350,425,(0,0,0));   
                                    time.sleep(0.12);
                                if keyboard.is_pressed('space'):
                                    p2=p2+' ';
                                    pprint(str(p2),350,425,(0,0,0));   
                                    time.sleep(0.12);
                                elif keyboard.is_pressed('shift+'+str(alf[i])) and len(p2)<20:
                                    p2=p2+str(alf2[i])
                                    time.sleep(0.12);
                                    pprint(str(p2),350,425,(0,0,0));
                                elif keyboard.is_pressed(str(alf[i])) and len(p2)<20:
                                    p2=p2+str(alf[i]);
                                    time.sleep(0.12);
                                    pprint(str(p2),350,425,(0,0,0));
                    else:
                        if p2=='':
                            pprint('Password(again):',350,425,(0,0,0))
                        else:
                            pprint(str(p2),350,425,(0,0,0));
                            if un1!='' and p1!='' and p2!='' and p1==p2:
                                try:
                                    v0=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','r');
                                    v0.close();
                                    pprint('There is an User Name in this name, Please Write Something Else',10,10,(255,0,0))
                                    time.sleep(3);
                                    un1='';
                                    p1='';
                                    p2='';
                                    continue;
                                except:
                                    v0=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','w');
                                    v0.write(str(un1)+'\n'+str(p1)+'\n')
                                    v0.close();
                                    un1='';
                                    p1='';
                                    break;
                            elif un1!='' and p1!='' and p2!='':
                                pprint('Your Passwords are not the same, Please fix Them',10,10,(255,0,0))
                                time.sleep(3);
                                p1='';
                                p2='';
                                continue;           
                    pygame.display.update();
        else:
            gd.blit(login,(300,200))
        if (350<mouse[0]<535) and (305<mouse[1]<340) and (click[0]==1):
            while not keyboard.is_pressed('Enter'):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit();
                        exit();
                for i in range(len(alf)):
                    if keyboard.is_pressed('backspace'):
                        un1=un1[:(len(un1)-1)];
                        gd.fill((255,255,255))
                        if (400<mouse[0]<477) and (448<mouse[1]<485):
                            gd.blit(loginB,(300,200))
                        else:
                            gd.blit(login,(300,200))
                        pygame.display.update();
                        pprint(str(un1),350,315,(0,0,0));   
                        time.sleep(0.12);
                    if keyboard.is_pressed('space'):
                        un1=un1+' '
                        pprint(str(un1),350,315,(0,0,0));   
                        time.sleep(0.12);
                    elif keyboard.is_pressed('shift+'+str(alf[i])) and len(un1)<20:
                        un1=un1+str(alf2[i])
                        time.sleep(0.12);
                        pprint(str(un1),350,315,(0,0,0));
                    elif keyboard.is_pressed(str(alf[i])) and len(un1)<20:
                        un1=un1+str(alf[i]);
                        time.sleep(0.12);
                        pprint(str(un1),350,315,(0,0,0));
        else:
            if un1=='':
                pprint('User Name:',350,315,(0,0,0))
            else:
                pprint(str(un1),350,315,(0,0,0));
        if (350<mouse[0]<535) and (365<mouse[1]<400) and (click[0]==1):
            while not keyboard.is_pressed('Enter'):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit();
                        exit();
                for i in range(len(alf)):
                    if keyboard.is_pressed('backspace'):
                        p1=p1[:(len(p1)-1)];
                        gd.fill((255,255,255))
                        if (400<mouse[0]<477) and (448<mouse[1]<485):
                            gd.blit(loginB,(300,200))
                        else:
                            gd.blit(login,(300,200))
                        pygame.display.update();
                        pprint(str(p1),350,375,(0,0,0));   
                        time.sleep(0.12);
                    if keyboard.is_pressed('space'):
                        p1=p1+' '
                        pprint(str(p1),350,375,(0,0,0));   
                        time.sleep(0.12);
                    elif keyboard.is_pressed('shift+'+str(alf[i])) and len(p1)<20:
                        p1=p1+str(alf2[i])
                        time.sleep(0.12);
                        pprint(str(p1),350,375,(0,0,0));
                    elif keyboard.is_pressed(str(alf[i])) and len(p1)<20:
                        p1=p1+str(alf[i]);
                        time.sleep(0.12);
                        pprint(str(p1),350,375,(0,0,0));
        else:
            if p1=='':
                pprint('Password:',350,375,(0,0,0))
            else:
                pprint(str(p1),350,375,(0,0,0));
                if un1!='' and p1!='':
                    try:
                        v1=open('Cezar Mail Kisiler\\'+str(un1)+'.txt','r');
                        c=v1.readlines(2);
                        username=(str(c[0][:len(c[0])-1]));
                        password=(str(c[1]));
                    except:
                        pprint('This User Name can not be found, Please try again.',10,10,(255,0,0))
                        time.sleep(3);
                        un1='';
                        p1='';
                        continue;
                    if (str(un1)!=username) or ((str(p1)+'\n')!=password):
                        pprint('User Name or Password is incorrect.',10,10,(255,0,0));
                        time.sleep(3);
                        un1='';
                        p1='';
                        continue;
                    while True:
                        mouse = pygame.mouse.get_pos();
                        click = pygame.mouse.get_pressed();
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit();
                                exit();
                        gd.fill((200,200,200));
                        gd.blit(logo,(10,10));
                        gd.blit(Page,(10,100));
                        pprint('Welcome '+str(un1),700,130,(0,0,0));
                        if ((14<mouse[0]<150) and (175<mouse[1]<195)) and (click[0]==1):
                            un1=''
                            p1=''
                            p2=''
                            break;
                        gmail_posts();
                        Postalar(un1,p1)
                        if (160<mouse[0]<285) and (113<mouse[1]<165) and(click[0]==1):
                            du=0;
                            while True:
                                mouse = pygame.mouse.get_pos();
                                click = pygame.mouse.get_pressed();
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit();
                                        exit();
                                if du==0:
                                    gd.fill((200,200,200));
                                    gd.blit(logo,(10,10));
                                    gd.blit(Page,(10,100));
                                    pygame.draw.rect(gd,(255,255,255),[170,170,500,56]);
                                    pygame.draw.rect(gd,(255,255,255),[170,231,500,56]);
                                    pygame.display.update();
                                    pprint('Welcome '+str(un1),700,130,(0,0,0));
                                    pprint('Exit',15,180,(0,0,0))
                                    pprint('Snake Game',175,193,(0,0,0))
                                    pprint('Pong',175,254,(0,0,0))
                                    du=1;
                                if ((170<mouse[0]<670) and (230<mouse[1]<286)) and (click[0]==1):
                                    Oyun_Pong();
                                    du=0;
                                if ((170<mouse[0]<670) and (170<mouse[1]<226)) and (click[0]==1):
                                    Oyun_Snake();
                                    du=0;
                                if ((14<mouse[0]<150) and (175<mouse[1]<195)) and (click[0]==1):
                                    break;
                                if ((10<mouse[0]<145) and (102<mouse[1]<170)) and (click[0]==1):
                                    break;
                                time.sleep(0.1);
                                pygame.display.update();
                        if(13<mouse[0]<50) and (308<mouse[1]<325) and (click[0]==1):
                            an1=''
                            pa=''
                            break;
                        if (10<mouse[0]<145) and (102<mouse[1]<170) and(click[0]==1):
                            text='';
                            per='';
                            while True:
                                mouse = pygame.mouse.get_pos();
                                click = pygame.mouse.get_pressed();
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit();
                                        exit();
                                gd.blit(New,(600,200));
                                if (600<mouse[0]<640) and (200<mouse[1]<230) and (click[0]==1):
                                    gd.fill((200,200,200));
                                    gd.blit(logo,(10,10));
                                    gd.blit(Page,(10,100));
                                    pprint('Welcome '+str(un1),700,130,(0,0,0));
                                    gd.blit(New,(600,200));
                                    pygame.display.update();
                                    for j in range(int(len(text)/25)+1):
                                        pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                    pprint(str(per),610,205,(0,0,0));
                                    while not keyboard.is_pressed('Enter'):
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit();
                                                exit();
                                        for i in range(len(alf)):
                                            if keyboard.is_pressed('backspace'):
                                                per=per[:(len(per)-1)];
                                                gd.fill((200,200,200));
                                                gd.blit(logo,(10,10));
                                                gd.blit(Page,(10,100));
                                                pprint('Welcome '+str(un1),700,130,(0,0,0));
                                                gd.blit(New,(600,200));
                                                pygame.display.update();
                                                for j in range(int(len(text)/25)+1):
                                                    pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                                pprint(str(per),610,205,(0,0,0));
                                                time.sleep(0.1);
                                            if keyboard.is_pressed('space') and len(per)<20:
                                                per=per+' ';
                                                gd.fill((200,200,200));
                                                gd.blit(logo,(10,10));
                                                gd.blit(Page,(10,100));
                                                pprint('Welcome '+str(un1),700,130,(0,0,0));
                                                gd.blit(New,(600,200));
                                                pygame.display.update();
                                                for j in range(int(len(text)/25)+1):
                                                    pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                                pprint(str(per),610,205,(0,0,0));
                                                time.sleep(0.1);
                                            elif keyboard.is_pressed('shift+'+str(alf[i])) and len(per)<20:
                                                per=per+str(alf2[i])
                                                time.sleep(0.1);
                                                pprint(str(per),610,205,(0,0,0));
                                            elif keyboard.is_pressed(str(alf[i])) and len(per)<20:
                                                per=per+str(alf[i]);
                                                time.sleep(0.1);
                                                gd.fill((200,200,200));
                                                gd.blit(logo,(10,10));
                                                gd.blit(Page,(10,100));
                                                pprint('Welcome '+str(un1),700,130,(0,0,0));
                                                gd.blit(New,(600,200));
                                                pygame.display.update();
                                                for j in range(int(len(text)/25)+1):
                                                    pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                                pprint(str(per),610,205,(0,0,0));
                                else:
                                    if per=='':
                                        pprint('For:',610,205,(0,0,0))
                                    else:
                                        pprint(str(per),610,205,(0,0,0));
                                    if text=='':
                                        pprint('Text:',610,260,(0,0,0))
                                    else:
                                        for j in range(int(len(text)/25)+1):
                                            pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                if (600<mouse[0]<640) and (260<mouse[1]<270) and (click[0]==1):
                                    eylem=0;
                                    gd.fill((200,200,200));
                                    gd.blit(logo,(10,10));
                                    gd.blit(Page,(10,100));
                                    pprint('Welcome '+str(un1),700,130,(0,0,0));
                                    gd.blit(New,(600,200));
                                    pprint(str(per),610,205,(0,0,0));
                                    for j in range(int(len(text)/25)+1):
                                        pprint(str(text[(25*j):25+(25*j)]),610,260+(j+15),(0,0,0));
                                    while True:
                                        mouse = pygame.mouse.get_pos();
                                        click = pygame.mouse.get_pressed();
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit();
                                                exit();
                                        while not keyboard.is_pressed('Enter'):
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit();
                                                    exit();
                                            for i in range(len(alf)):
                                                if keyboard.is_pressed('backspace'):
                                                    text=text[:(len(text)-1)];
                                                    gd.fill((200,200,200));
                                                    gd.blit(logo,(10,10));
                                                    gd.blit(Page,(10,100));
                                                    pprint('Welcome '+str(un1),700,130,(0,0,0));
                                                    gd.blit(New,(600,200));
                                                    pygame.display.update();
                                                    pprint(str(per),610,205,(0,0,0));
                                                    for j in range(int(len(text)/25)+1):
                                                        pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                                    time.sleep(0.2);
                                                if keyboard.is_pressed('space') and len(text)<275:
                                                    text=text+' ';
                                                    gd.fill((200,200,200));
                                                    gd.blit(logo,(10,10));
                                                    gd.blit(Page,(10,100));
                                                    pprint('Welcome '+str(un1),700,130,(0,0,0));
                                                    gd.blit(New,(600,200));
                                                    pygame.display.update();
                                                    pprint(str(per),610,205,(0,0,0));
                                                    for j in range(int(len(text)/25)+1):
                                                        pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                                    time.sleep(0.1);
                                                elif keyboard.is_pressed('shift+'+str(alf[i])) and len(text)<275:
                                                    text=text+str(alf2[i])
                                                    time.sleep(0.1);
                                                    pprint(str(per),610,205,(0,0,0));
                                                    for j in range(int(len(text)/25)+1):
                                                        pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                                elif keyboard.is_pressed(str(alf[i])) and len(text)<275:
                                                    text=text+str(alf[i]);
                                                    time.sleep(0.1);
                                                    gd.fill((200,200,200));
                                                    gd.blit(logo,(10,10));
                                                    gd.blit(Page,(10,100));
                                                    pprint('Welcome '+str(un1),700,130,(0,0,0));
                                                    gd.blit(New,(600,200));
                                                    pygame.display.update();
                                                    pprint(str(per),610,205,(0,0,0));
                                                    for j in range(int(len(text)/25)+1):
                                                        pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                        break;
                                else:
                                    if text=='':
                                        pprint('Text:',610,260,(0,0,0))
                                    else:
                                        for j in range(int(len(text)/25)+1):
                                            pprint(str(text[(25*j):25+(25*j)]),610,260+(j*15),(0,0,0));
                                if(847<mouse[0]<865) and (440<mouse[1]<465) and (click[0]==1):
                                    break;
                                if(13<mouse[0]<50) and (308<mouse[1]<325) and (click[0]==1):
                                    break;
                                if(626<mouse[0]<690) and (435<mouse[1]<460) and (click[0]==1):
                                    for i in range(len(per)):
                                        if per[i:]=='gmail':
                                            eylem=1
                                            try:
                                                import smtplib
                                                mail=smtplib.SMTP('smtp.gmail.com',587)
                                                mail.ehlo()
                                                mail.starttls()
                                                print(str(per[:i]))
                                                mail.login('cezarmail.cmail@gmail.com','password');
                                                mail.sendmail('cezarmail.cmail@gmail.com',str(per[:i])+'@gmail.com','To:'+str(per[:i])+'\nFrom:cezarmail.cmail@gmail.com\nSubject:From:'+str(un1)+'\n'+str(text))
                                                mail.close();
                                                #print(https://www.google.com/settings/security/lesssecureapps);
                                                break;
                                            except:
                                                pprint('No Internet',150,10,(255,0,0));
                                                time.sleep(1);
                                                break;
                                    if eylem==0:
                                        sifrele(str(un1),str(text),str(per))
                                    time.sleep(1);
                                    break;
                                pygame.display.update();  
                        pygame.display.update();
        pygame.display.update();
CezarMail_loop();
