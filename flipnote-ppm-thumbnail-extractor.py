import os
import sys
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk

openedfile = None
openedfiledata = None
openedppmthumb = None
thmb = None
show_stuff = False

tk = tkinter.Tk()
size = tk.geometry("150x200")
tkolor = tk.configure(background='#ff6300')
tkitle = tk.title("Flipnote PPM Thumbnail Extractor")

def openfilefunc():
	global openedfile, openedfiledata, openedppmthumb, thmb, show_stuff
	prevopenedfile = openedfile
	openedfile = filedialog.askopenfilenames(filetypes=[("Flipnote PPM", "*.ppm")])
	if openedfile == (""):
		openedfile = prevopenedfile
	else:
		openedfiledata = [None] * len(openedfile)
		thmb = [None] * (len(openedfile) + 1)
		openedppmthumb = [None] * len(openedfile)
		for i in range(len(openedfile)):
			with open(openedfile[i], "rb") as f:
				openedfiledata[i] = f.read(1696).hex()
	for i in range(len(openedfiledata)):
		openedppmthumb[i] = openedfiledata[i][320:]
	
	for n in range(len(openedppmthumb) + 1):
		thmb[n] = Image.new('P', (64, 48))
		thmb[n].putpalette([0xff, 0xff, 0xff, 0x52, 0x52, 0x52, 0xff, 0xff, 0xff, 0x9c, 0x9c, 0x9c, 0xff, 0x48, 0x44, 0xc8, 0x51, 0x4f, 0xff, 0xad, 0xac, 0x00, 0xff, 0x00, 0x48, 0x40, 0xff, 0x51, 0x4f, 0xb8, 0xad, 0xab, 0xff, 0x00, 0xff, 0x00, 0xb6, 0x57, 0xb7, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00])
		
		k = -4
		
		if n != len(openedppmthumb):
			openedppmthumbdata = openedppmthumb[n]
		else:
			openedppmthumbdata = ("11111111a1aaaaaaa1222222a1222222"
								  "a1222222a1222222a1222222a1222222"
							      "11111111aaaaaaaa2222222222222222"
							      "22222222222222222282228222822282"
							      "11111111aaaaaaaa2222222222222222"
							      "22222222222222222222228222222282"
							      "11111111aaaaaaaa2222222222222222"
							      "22222222222222222222222222822282"
							      "11111111aaaaaaaa2222222222222222"
							      "22222222222222222222228222222282"
							      "11111111aaaaaaaa2222222222222222"
							      "22222222222222222222222222222222"
							      "11111111aaaaaaaa2222222222222222"
							      "22222222222222222222222222222222"
							      "113333331a3333331a3333331a113133"
							      "1aaa31331aa231331aa211111aa2a11a"
							      "a1222222a1222222a1222222a1222222"
							      "a1222222a1222222a1222222a1222222"
							      "22822888228228882282828222828282"
							      "22822282228222822282228222222222"
							      "22222282822282828222828282228282"
							      "82228282822282822288882222222222"
							      "22822222228888822282228222822282"
							      "22822282228222822822888222222222"
							      "22222282828828828222828282228282"
							      "82228282828828828222222282222222"
							      "22222222228288222228222822888828"
							      "22282222222822222882882822222222"
							      "22222222222222222222222222222222"
							      "22222222222222222222222222222222"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "a1222222a1222222a1222222a1222222"
							      "a1222222a1222222a1222222a1222222"
							      "22222222222222222222222222222222"
							      "22222222222222222222222222222222"
							      "22888828222822222228222222282222"
							      "22888828222822222228222222282222"
							      "22282222282822222228222228282288"
							      "28288222282882882828822228288222"
							      "22222222222222222222222228228828"
							      "82822222882288222222222822222228"
							      "22222222222222222222222222222222"
							      "22222222222222222222222222222222"
							      "22222222222222222222222222222222"
							      "22222222222222222222222222222222"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "a1222222a1222222a1222222a1222222"
							      "a1222222a1222222a1222222a1222222"
							      "22222222222222228288222228222222"
							      "28222222282222888228822222828288"
							      "22282222222222222282222222822222"
							      "22822222288222828282222888822288"
							      "28822288222222222222222222222222"
							      "22222222882282882228282288282822"
							      "88828822222222222222222222822222"
							      "22822222288888222282228222822282"
							      "22222222222222222222222222222222"
							      "22222222882822882282822288888222"
							      "22222222222222228222222282222222"
							      "82222222882222228222222282222222"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "a1222222a1222222a1222222a1222222"
							      "a1222222a1222222a1222222a1222222"
							      "22828222228282228828228822222222"
							      "22222222222222222222222222222222"
							      "22822228228222288822288222222222"
							      "22222222222222222222222222222222"
							      "22222822222228228828828822222222"
							      "22222222222222222222222222222222"
							      "22822282228222822822882222222222"
							      "22222222222222222222222222222222"
							      "22228222222282228888228822222222"
							      "22222222222222222222222222222222"
							      "82222222822222228822222222222222"
							      "22222222222222222222222222222222"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "1aa2211a1aa2211a1aa2211a1aa2211a"
							      "a1aaaaaa1111111133132a223313aaaa"
							      "33131111333333a1333333a133333311"
							      "aaaaaaaa1111111122222222aaaaaaaa"
							      "1111111122222222aaaaaaaa11111111"
							      "aaaaaaaa1111111122222222aaaaaaaa"
							      "1111111122222222aaaaaaaa11111111"
							      "aaaaaaaa1111111122222222aaaaaaaa"
							      "1111111122222222aaaaaaaa11111111"
							      "aaaaaaaa1111111122222222aaaaaaaa"
							      "1111111122222222aaaaaaaa11111111"
							      "aaaaaaaa1111111122222222aaaaaaaa"
							      "1111111122222222aaaaaaaa11111111"
							      "aaaaaaaa1111111122222222aaaaaaaa"
							      "1111111122222222aaaaaaaa11111111"
							      "1aa2211a11a2211a22a2211aaaaa211a"
							      "1111211a2222221aaaaaaa1a11111111")
		
		for m in range(6):
			for l in range(8):
				for j in range(8):
					for i in range(2):
						k = k+4
						thmb[n].putpixel(((i*4)+(l*8)+1, j+(m*8)), int(openedppmthumbdata[k], 16))
						thmb[n].putpixel(((i*4)+(l*8)+0, j+(m*8)), int(openedppmthumbdata[k+1], 16))
						thmb[n].putpixel(((i*4)+(l*8)+3, j+(m*8)), int(openedppmthumbdata[k+2], 16))
						thmb[n].putpixel(((i*4)+(l*8)+2, j+(m*8)), int(openedppmthumbdata[k+3], 16))
				
		if n != len(openedppmthumb):
			print("Opened PPM file at " + openedfile[n])
	
	if len(openedppmthumb) == 1:
		thmbimtk = ImageTk.PhotoImage(thmb[0])
		tim.configure(image=thmbimtk)
		tim.photo_ref = thmbimtk
	else:
		thmbimtk = ImageTk.PhotoImage(thmb[-1])
		tim.configure(image=thmbimtk)
		tim.photo_ref = thmbimtk
	
	if show_stuff == False:
		show_stuff = True
		br1.pack()
		tim.pack()
		br2.pack()
		qsv.pack()
		msv.pack()

def quicksave():
	for i in range(len(thmb) - 1):
		thmb[i].save(openedfile[i][:-4] + ".png","PNG")
		print("Thumbnail saved to " + openedfile[i][:-4] + ".png")

def womansave(): # ok the thought process on this name:
	# "manualsave" can be shortened into "mansave"
	# but then it has "man" at the beginning
	# and we should be more feminist
	# so i should change that to "womansave"
	# IT MAKES SENSE OKAY /silly
	if (len(thmb) - 1) != 1:
		savetofile = filedialog.asksaveasfile(mode='w', initialfile=os.path.basename("ONLY_FILE_TYPE_AND_LOCATION_SAVED.png"), defaultextension=".*", filetypes=[("PNG's Not GIF", "*.png"), ("/ɡɪf/", "*.gif"), ("Bitmap. Marvelous Picformat.", "*.bmp *.dib"), ("Tag Image File Format", "*.tiff *.tif"), ("Why Even Bother Picformat", "*.webp")])
	else:
		savetofile = filedialog.asksaveasfile(mode='w', initialfile=os.path.basename(openedfile[0][:-4] + ".png"), defaultextension=".*", filetypes=[("PNG's Not GIF", "*.png"), ("/ɡɪf/", "*.gif"), ("Bitmap. Marvelous Picformat.", "*.bmp *.dib"), ("Tag Image File Format", "*.tiff *.tif"), ("Why Even Bother Picformat", "*.webp")])
	os.remove(savetofile.name)
	# Unused bc i dont feel like figuring it out
	# , ("Joint Photographic Expert Group", "*.jpg *.jpeg")
	if savetofile.name != "":
		if savetofile.name[-4:] == ".png":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".png"), "PNG")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".png"))
			else:
				thmb[0].save(savetofile.name, "PNG")
				print("Thumbnail saved to " + savetofile.name)
		#elif savetofile.name[-4:] == ".jpg":
			#thmb.save(savetofile.name, "JPEG")
			#print("Thumbnail saved to " + savetofile.name)
		elif savetofile.name[-4:] == ".gif":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".gif"), "GIF")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".gif"))
			else:
				thmb[0].save(savetofile.name, "GIF")
				print("Thumbnail saved to " + savetofile.name)
		elif savetofile.name[-4:] == ".bmp":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".bmp"), "BMP")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".bmp"))
			else:
				thmb[0].save(savetofile.name, "BMP")
				print("Thumbnail saved to " + savetofile.name)
		elif savetofile.name[-4:] == ".dib":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".dib"), "BMP")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".dib"))
			else:
				thmb[0].save(savetofile.name, "BMP")
				print("Thumbnail saved to " + savetofile.name)
		elif savetofile.name[-4:] == ".tif":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".tif"), "TIFF")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".tif"))
			else:
				thmb[0].save(savetofile.name, "TIFF")
				print("Thumbnail saved to " + savetofile.name)
		#elif savetofile.name[-5:] == ".jpeg":
			#thmb.save(savetofile.name, "JPEG")
			#print("Thumbnail saved to " + savetofile.name)
		elif savetofile.name[-5:] == ".tiff":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".tiff"), "TIFF")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".tiff"))
			else:
				thmb[0].save(savetofile.name, "TIFF")
				print("Thumbnail saved to " + savetofile.name)
		elif savetofile.name[-5:] == ".webp":
			if (len(thmb) - 1) != 1:
				for i in range(len(thmb) - 1):
					thmb[i].save(os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".webp"), "WEBP")
					print("Thumbnail saved to " + os.path.join(os.path.dirname(savetofile.name), os.path.basename(openedfile[i])[:-4] + ".webp"))
			else:
				thmb[0].save(savetofile.name, "WEBP")
				print("Thumbnail saved to " + savetofile.name)
		else:
			print("Thumbnail not saved due to invalid file format which shouldn't be able to happen but here we are 0_0\n(Attempted save location was" + savetofile.name + ")")

ofi = tkinter.Button(text="Open File",command=openfilefunc)
ofi.configure(background='#84c600', activebackground="#c6e784")
ofi.pack()

br1 = tkinter.Label(text="")
br1.configure(background='#ff6300')

tim = tkinter.Label(image=None)
tim.configure(borderwidth=0)

br2 = tkinter.Label(text="")
br2.configure(background='#ff6300')

qsv = tkinter.Button(text="Quick Save",command=quicksave)
qsv.configure(background='#84c600', activebackground="#c6e784")

msv = tkinter.Button(text="Manual Save",command=womansave)
msv.configure(background='#84c600', activebackground="#c6e784")

# Main Loop
tk.mainloop()
