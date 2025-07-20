import requests
import os
import shutil
import numpy as np
from PIL import Image, ImageSequence
from PIL.Image import Palette
from guizero import App, Text, PushButton, Window, TextBox

app = App(title="C3TS Civ 3 Tileset")
space = Text(app, text="")
text1 = Text(app, text="Choose C3TS Input File")
space1 = Text(app, text="")
textbox1 = TextBox(app, text="Civ 3 Full.c3ts")

"""
"Idle", default
"Pollution", Irrigate
"Mine", Mine
"Irrigate", Irrigate
"Fortified", fortify hold
"Pillage", Victory
"Transform", 
"Fortifying", Fortify
"Fallout", Irrigate
"Clean", Irrigate
"Base", Fortress Build
"Road", Road
"Convert", Build
"Cultivate", Irrigate
"Plant", Plant, Irrigate
"""

def make_spec(tag, folder, frames, anims):
    spec = open(folder+tag+"/"+tag+".spec","w+")
    #print(anims)
    spec.write('''
;Made by Civ III Tileset for freeciv
;All graphics remain the property of their creators and are subject to their licenses

[spec]

; Format and options of this spec file:
options = "+Freeciv-spec-3.3-Devel-2023.Apr.05"

[info]

;

artists = "
    Civ III Graphics Community
"

[extra]
sprites =
{	"tag", "file"\n''')
    for anim in anims:
        #print(anim)
        for i in range(frames):
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_s:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_s:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_se:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_se:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_e:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_e:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_ne:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_ne:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_n:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_n:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_nw:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_nw:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_w:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_w:'+str(i)+'"\n')
            spec.write('		"u.'+tag[2:len(tag)]+'_'+anim+'_sw:'+str(i)+'", "Civ 3 Full/'+folder+tag+'/final_'+tag+'_'+anim+'_sw:'+str(i)+'"\n')
    spec.write('''		}\n''')
    spec.close()



    

def convert_img_bg(pic):
    p=pic.getpalette()
    for i in range(len(p)-1, (256*3)-1):
        p.append(0)
#     print(p)
    palette = np.array(p, dtype=np.uint8).reshape((256,3))
    alpha = [
        [25, 0, 25],
        [40,0,40],
        [56,0,56],
        [70,0,70],
        [100,0,100],
        [100,0,100],
        [100,0,100],
        [100,0,100],
        [100,0,100],
        [120,0,120],
        [140,0,140],
        [160,0,160],
        [180,0,180],
        [200,0,200],
        [220,0,220],
        [255,0,255],
        [255,0,255],
        [255,0,255],
        [255,0,255]
        ]
    new_palette = []
    a=0
    i=0
    for colour in palette:
        i += 1
        if i < 239:
            new_palette.append(colour[0])
            new_palette.append(colour[1])
            new_palette.append(colour[2])
            #new_palette.append(255)
        else:
            new_palette.append(alpha[a][0])
            new_palette.append(alpha[a][1])
            new_palette.append(alpha[a][2])
            #new_palette.append(alpha[a][3])
            a+=1
    pic.putpalette(new_palette, rawmode="RGB")
    return pic

def convert_to_transparent(path, output_dir, tag, direction, anim, frame):
    pic = Image.open(path)
    pic = pic.quantize(colors=128)
    p=pic.getpalette()
    for i in range(len(p)-1, (256*3)-1):
        p.append(0)
    palette = np.array(p, dtype=np.uint8).reshape((256,3))
    new_palette = []
    for colour in palette:
        if colour[0] == colour[2]+1 or colour[0] == colour[2] and colour[1] <= colour[0]/2:
            new_palette.append(colour[0])
            new_palette.append(colour[0])
            new_palette.append(colour[0])
            new_palette.append(255 - colour[0])
        else:
            new_palette.append(colour[0])
            new_palette.append(colour[1])
            new_palette.append(colour[2])
            new_palette.append(255)
    pic.putpalette(new_palette, rawmode="RGBA")
    new_image = Image.new("RGBA", (240, 240), color=(0,0,0,0))
    new_image.paste(pic, box=(int(120-pic.width/2), int(120-pic.height/2)))
    new_image.save(output_dir+tag+"/final_"+tag+"_"+anim+"_"+direction+":"+str(frame)+".png")
    
def crop_to_cimpletoon(path, name, outputpath, frame=0):
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    imgs   =  {}
    imgs["sw"] = Image.open(path+"/d_sw:"+str(frame)+".png")
    imgs["s"]  = Image.open(path+"/d_s:"+str(frame)+".png")
    imgs["se"] = Image.open(path+"/d_se:"+str(frame)+".png")
    imgs["e"]  = Image.open(path+"/d_e:"+str(frame)+".png")
    imgs["ne"] = Image.open(path+"/d_ne:"+str(frame)+".png")
    imgs["n"]  = Image.open(path+"/d_n:"+str(frame)+".png")
    imgs["nw"] = Image.open(path+"/d_nw:"+str(frame)+".png")
    imgs["w"]  = Image.open(path+"/d_w:"+str(frame)+".png")

    for img in imgs:
        #print("next pic")
        zero = imgs[img].getpixel((0,0))
        for x in range(imgs[img].width):
            for y in range(imgs[img].height):
                if imgs[img].getpixel((x,y)) == zero:
                    pass
                else:
                    if x > maxx:
                        maxx = x
                    if x < minx or minx == 0:
                        minx = x
                    if y > maxy:
                        maxy = y
                    if y < miny or miny == 0:
                        miny = y
    print([minx, maxx, miny, maxy])
    print("\n")
    if (maxx-minx)/64 > (maxy-miny)/48:
        yoffset = (48*((maxx-minx)/64)-(maxy-miny))/2
        for img in imgs:
            to_be_saved = imgs[img].crop((minx, miny-yoffset, maxx, maxy+yoffset)).copy()
            to_be_saved.save(path+"/cropped_"+img+".png")
            to_be_saved.resize((64,48), resample=Image.LANCZOS).save((outputpath+name+"/final_"+name+"_"+img+".png"))
    if (maxx-minx)/64 < (maxy-miny)/48:
        xoffset = (64*((maxy-miny)/48)-(maxx-minx))/2
        for img in imgs:
            to_be_saved = imgs[img].crop((minx-xoffset, miny, maxx+xoffset, maxy)).copy()
            to_be_saved.save(path+"/cropped_"+img+".png")
            to_be_saved.resize((64,48), resample=Image.LANCZOS).save((outputpath+name+"/final_"+name+"_"+img+".png"))
    make_spec(name, outputpath)

def convert():
    units=open(textbox1.value, "r")
    line_num=0
    finalPath="output/tileset/"
    tags=[]
    urls=[]
    for line in units:
        if line[0] == "h":
            urls.append(line)
        elif line[0] == "u":
            tags.append(line)
        elif line[0] == "P":
            finalPath = line[1:len(line)].strip()
        elif line[0] == "C":
            finalPath =  line.strip()
        else:
            pass
        
    for link in urls:
        tag = tags[urls.index(link)].strip()
        cwd = os.getcwd()
        if not os.path.exists(cwd+"/output/tileset/"+tag):
            os.makedirs(cwd+"/output/tileset/"+tag)
        if not os.path.exists(cwd+"/"+finalPath+tag):
            os.makedirs(cwd+"/"+finalPath+tag)
        if os.path.exists(tag+".rar") == False:
            file = requests.get(link)
            open(tag+".rar", "wb").write(file.content)
        if os.name == "nt":
            os.system('cmd /c "7z.exe e "'+tag+'".rar -ooutput/temp/"'+tag+'" -y"')
        if os.name == "posix":
            print('./output/temp/'+tag)
            if os.path.exists('./output/temp/'+tag) == False:
                #os.system('7za e "'+tag+'".rar -ooutput/temp/"'+tag+'" -y')
                os.system('file-roller --force -e "./output/temp/'+tag+'" '+tag+'.rar')
            print(len(os.listdir("output/temp/"+tag)))
            for path in os.listdir("output/temp/"+tag):
                if os.path.isdir("output/temp/"+tag+"/"+path):
                    print(path)
                    for path2 in os.listdir("output/temp/"+tag+"/"+path):
                        print("output/temp/"+tag+"/"+path+"/"+path2)
                        print("output/temp/"+tag+"/"+path2)
                        if os.path.exists("output/temp/"+tag+"/"+path2) == False:
                            os.rename("output/temp/"+tag+"/"+path+"/"+path2, "output/temp/"+tag+"/"+path2)
        else:
            raise Exception("Sorry, OS is not supported")
        
        anims = {}
        
        for file in os.listdir("output/temp/"+tag):
            #print(file)
            if file.endswith(".INI") or file.endswith(".ini"):
                ini = open("output/temp/"+tag+"/"+file)
                ini = ini.read()
                ini = ini.splitlines()
                #print(ini)
                for line in ini:
                    if line.startswith("DEFAULT") and line.endswith('.flc'):
                        anims["Idle"]=line.split("=")[1]
                    if line.startswith("IRRIGATE") and line.endswith('.flc'):
                        filename=line.split("=")[1]
                        anims["Pollution"]=filename
                        anims["Irrigate"]=filename
                        anims["Fallout"]=filename
                        anims["Clean"]=filename
                        anims["Cultivate"]=filename
                    if line.startswith("MINE") and line.endswith('.flc'):
                        anims["Mine"]=line.split("=")[1]
                    if line.startswith("FORTIFY") and line.endswith('.flc'):
                        anims["Fortifying"]=line.split("=")[1]
                        anims["Fortified"]=line.split("=")[1]
                    if line.startswith("VICTORY") and line.endswith('.flc'):
                        anims["Pillage"]=line.split("=")[1]
                    if line.startswith("FORTRESS") and line.endswith('.flc'):
                        anims["Base"]=line.split("=")[1]
                    if line.startswith("ROAD") and line.endswith('.flc'):
                        anims["Road"]=line.split("=")[1]
                    if line.startswith("BUILD") and line.endswith('.flc'):
                        anims["Convert"]=line.split("=")[1]
        #print(anims)
        
        if len(anims) == 0:
            anims["Idle"]="Default.flc"
        
        for anim in anims:
            #print(anim)
            file = anims[anim]
            try:
                temp_img = Image.open("output/temp/"+tag+"/"+file)
            except FileNotFoundError:
                temp_img = Image.open("output/temp/"+tag+"/"+file.capitalize())
            try:
                temp_img.save("output/temp/"+tag+"/"+file+".gif", save_all=True, loop=0)
            except OSError:
                print("Couldn't Save GIF File")
            else:
                convert_img_bg(temp_img).save("output/temp/"+tag+"/test.gif", save_all=True, loop=0)
                img = temp_img.copy()
                gif = Image.open("output/temp/"+tag+"/test.gif")
                #print(gif.is_animated)
                #print("frames: "+str(gif.n_frames))
                frame_loc = 0
                #anim="Idle"
                for frame in ImageSequence.Iterator(gif):
                    if frame_loc <= int(gif.n_frames/8):
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_s:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_s:"+str(frame_loc)+".png", finalPath, tag, "s", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)+1 and frame_loc < int(gif.n_frames/8)*2+2:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_se:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_se:"+str(frame_loc)+".png", finalPath, tag, "se", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)*2+2 and frame_loc < int(gif.n_frames/8)*3+3:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_e:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_e:"+str(frame_loc)+".png", finalPath, tag, "e", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)*3+3 and frame_loc < int(gif.n_frames/8)*4+4:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_ne:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_ne:"+str(frame_loc)+".png", finalPath, tag, "ne", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)*3+3 and frame_loc < int(gif.n_frames/8)*4+4:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_n:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_n:"+str(frame_loc)+".png", finalPath, tag, "n", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)*3+3 and frame_loc < int(gif.n_frames/8)*4+4:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_nw:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_nw:"+str(frame_loc)+".png", finalPath, tag, "nw", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)*3+3 and frame_loc < int(gif.n_frames/8)*4+4:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_w:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_w:"+str(frame_loc)+".png", finalPath, tag, "w", anim, int(frame_loc%(gif.n_frames/8)))
                    if frame_loc >= int(gif.n_frames/8)*3+3 and frame_loc < int(gif.n_frames/8)*4+4:
                        try:
                            frame.save("output/tileset/"+tag+"/d_"+anim+"_sw:"+str(frame_loc)+".png")
                        except OSError:
                           #End of sequence
                           print("Couldn't Save PNG File")
                        #print("Saving file from anim: "+anim)
                        convert_to_transparent("output/tileset/"+tag+"/d_"+anim+"_sw:"+str(frame_loc)+".png", finalPath, tag, "sw", anim, int(frame_loc%(gif.n_frames/8)))


                    frame_loc += 1
                make_spec(tag, finalPath, int(gif.n_frames/8), anims)

space2 = Text(app, text="")
button1 = PushButton(app, text="Convert", command=convert)
app.display()
    
