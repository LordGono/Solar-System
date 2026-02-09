#from IPython.display import Image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.widgets import TextBox, RadioButtons


#---------Variables---------#|
Nframes = 365               #|
rad = 50                    #|
tinterval = 1000            #|
radEarthP = 0.9832899       #|
radEarthA = 1.0167103       #|
radEarth = 1.0              #|
framesEarth = 365           #|
eEarth = 0.0167				#|
radMoonP = 0.00242382       #|
radMoonA = 0.00270992       #|
radMoon = 0.00257           #|
framesMoon = 27             #|
eMoon = 0.0549				#|
radSun = 0.0                #|
radMercuryP = 0.307499      #|
radMercuryA = 0.466697      #|
radMercury = 0.387098       #|
framesMercury = 88          #|
eMercury = 0.205630			#|
radVenusP = 0.718440        #|
radVenusA = 0.728213        #|
radVenus = 0.723332         #|
framesVenus = 225           #|
eVenus = 0.0068				#|
radMarsP = 1.382            #|
radMarsA = 1.666            #|
radMars = 1.523679          #|
framesMars = 687            #|
eMars = 0.0934				#|
radPhobosP = 0.000061728    #|
radPhobosA = 0.0000063621   #|
radPhobos = 0.0000626746    #|
framesPhobos = 10 #0.318910 #|
ePhobos = 0.0151			#|
radDeimosP = 0.000156790    #|
radDeimosA = 0.000156893    #|
radDeimos = 0.000156841     #|
framesDeimos = 10 #1.3513   #|
eDeimos = 0.00033			#|
radVestaP = 2.15221         #|
radVestaA = 2.57138         #|
radVesta = 2.36179          #|
framesVesta = 1326          #|
eVesta = 0.0887				#|
radCeresP = 2.5577          #|
radCeresA = 2.9773          #|
radCeres = 2.7675           #|
framesCeres = 1682          #|
eCeres = 0.0758				#|
radJupiterP = 4.9501        #|
radJupiterA = 5.4588        #|
radJupiter = 5.2044         #|
framesJupiter = 4333        #|
eJupiter = 0.0484			#|
radIoP = 0.002807           #|
radIoA = 0.002830           #|
radIo = 0.002819            #|
framesIo = 20 #1.769        #|
eIo = 0.0041				#|
radEuropaP = 0.00444        #|
radEuropaA = 0.004525       #|
radEuropa = 0.004484        #|
framesEuropa = 20 #3.551    #|
eEuropa = 0.0094			#|
radGanymedeP = 0.007147     #|
radGanymedeA = 0.00716319   #|
radGanymede = 0.00715517    #|
framesGanymede = 25 #7.154  #|
eGanymede = 0.0011			#|
radCallistoP = 0.012493     #|
radCallistoA = 0.012680     #|
radCallisto = 0.012585      #|
framesCallisto = 27 #16.689 #|
eCallisto = 0.0074			#|
radSaturnP = 9.0412         #|
radSaturnA = 10.1238        #|
radSaturn = 9.5826          #|
framesSaturn = 10759        #|
eSaturn = 0.0541			#|
radIapetusP = 0				#|
radIapetusA = 0				#|
radIapetus = 0				#|
framesIapetus = 80			#|
eIapetus = 0.0286125		#|
radTitanP = 0.00793			#|
radTitanA = 0.00840			#|
radTitan = 0.00816			#|
framesTitan = 16			#|
eTitan = 0.0288				#|
radRheaP = 0				#|
radRheaA = 0				#|
radRhea = 0					#|
framesRhea = 0				#|
eRhea =	0					#|
radDioneP = 0				#|
radDioneA = 0				#|
radDione = 0				#|
framesDione = 0				#|
eDione = 0					#|
radTethysP = 0				#|
radTethysA = 0				#|
radTethys = 0				#|
framesTethys = 0			#|
eTethys = 0					#|
radEnceladusP = 0.001590	#|
radEnceladusA = 0.001620	#|
radEnceladus = 0.001590		#|
framesEnceladus = 9 #1.370	#|
eEnceladus = 0				#|
radMimasP = 0				#|
radMimasA = 0				#|
radMimas = 0				#|
framesMimas = 0				#|
eMimas = 0					#|
radUranusP = 18.33          #|
radUranusA = 20.11          #|
radUranus = 19.2184         #|
framesUranus = 30689        #|
eUranus = 0.0472			#|
radMirandaP = 0.000864		#|
radMirandaA = 0.000913		#|
radMiranda = 0.000900		#|
framesMiranda = 10 #1.413479#|
eMiranda = 0.0013			#|
radNeptuneP = 29.81         #|
radNeptuneA = 30.33         #|
radNeptune = 30.110387      #|
framesNeptune = 60182       #|
eNeptune = 0.0086			#|
radTritonA = 0.0023714		#|
radTritonP = 0.0021105		#|
radTriton = 0.002371415		#|
framesTriton = 8			#|
radPlutoP = 29.658          #|
radPlutoA = 49.305          #|
radPluto = 39.48            #|
framesPluto = 90560         #|
ePluto = 0.2488				#|
radHaumeaP = 34.952         #|
radHaumeaA = 51.483         #|
radHaumea = 43.218          #|
framesHaumea = 103774       #|
eHaumea = 0.1887			#|
radMakemakeP = 38.590       #|
radMakemakeA = 52.840       #|
radMakemake = 45.715        #|
framesMakemake = 112897     #|
eMakemake = 0.1559			#|
radHalleysP = 0.6           #|
radHalleysA = 35.0          #|
framesHalleys = 27492       #|
eHalleys = 0.9671			#|
#---------Variables---------#|





#----------------------------------------Figure Creation----------------------------------------#
fig = plt.figure(figsize=(10,10))
ax = plt.subplot2grid((3,3), (0,0), colspan=10, rowspan=10,
                       xlim=(-2.*rad, 2.*rad), ylim=(-2.*rad, 2.*rad), aspect='equal')
ax.set_adjustable('box')
#----------------------------------------Figure Creation----------------------------------------#





#----------------------------------------Sun----------------------------------------#
circSun = plt.Circle((0,0), radius=radSun, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circSun)
ax.grid(False)
ax.axis('off')
suncircle, = ax.plot([], [], marker='o', ms=4, color='orange')

#Sun Animate
def suninit():
    suncircle.set_data([], [])
    return suncircle,
def sunanimate(i):
    t = 2.*np.pi*float(i/(Nframes - 1.))
    sun_x_marker = radSun*np.cos(t)
    sun_y_marker = radSun*np.sin(t)
    suncircle.set_data(sun_x_marker, sun_y_marker)
    return suncircle,

animsun = animation.FuncAnimation(fig, sunanimate, init_func=suninit, frames=Nframes, interval=tinterval)
#----------------------------------------Sun----------------------------------------#




#----------------------------------------Earth----------------------------------------#
circEarth = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radEarth, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circEarth)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Earthcircle, = ax.plot([], [], marker='o', ms=4, color='blue')
Earthline, = ax.plot([], [], lw=1, color='blue')
Earth_xdata = []
Earth_ydata = []
EarthC = radEarthA+radEarthP

#Earth Animate
def Earthinit():
    Earthcircle.set_data([], [])
    return Earthcircle,
def Earthanimate(i):
    t = 2.*np.pi*float(i/(framesEarth - 1.))
    Earth_x_marker = eEarth+(radEarthA*np.cos(t))
    Earth_y_marker = radEarthP*np.sin(t)
    Earthcircle.set_data(Earth_x_marker, Earth_y_marker)
    return Earthcircle,
def Earthlineinit():
	Earthline.set_data([], [])
	return Earthline,
def Earthlineanimate(i):
	t = 2.*np.pi*float(i/(framesEarth - 1.))
	Earth_x_marker = eEarth+(radEarthA*np.cos(t))
	Earth_y_marker = radEarthP*np.sin(t)
	Earth_xdata.append(Earth_x_marker)
	Earth_ydata.append(Earth_y_marker)
	Earthline.set_data(Earth_xdata, Earth_ydata)
	return Earthline,
	
animEarth = animation.FuncAnimation(fig, Earthanimate, init_func=Earthinit, frames=framesEarth, interval=tinterval)
animEarthline = animation.FuncAnimation(fig, Earthlineanimate, init_func=Earthlineinit, frames=framesEarth, interval=tinterval)



#----------------------------------------Moon----------------------------------------#
mooncircle, = ax.plot([], [], marker='o', ms=1, color='red')
moonline, = ax.plot([], [], lw=1, color='0.75')
moon_xdata = []
moon_ydata = []
MoonC = radMoonA+radMoonP

#Moon Animate
def mooninit():
    mooncircle.set_data([], [])
    return mooncircle,

def moonanimate(i):
    te = 2.*np.pi*float(i/(framesEarth - 1.))
    tm = 2.*np.pi*float(i/(framesMoon - 1.))
    earth_x_marker = eEarth+(radEarthA*np.cos(te))
    earth_y_marker = radEarthP*np.sin(te)
    moon_x_marker = (earth_x_marker)+(radMoonA*np.cos(tm))
    moon_y_marker = (earth_y_marker)+(radMoonP*np.sin(tm))
    mooncircle.set_data(moon_x_marker, moon_y_marker)
    return mooncircle,

def moonlineinit():
    moonline.set_data([], [])
    return moonline,

def moonlineanimate(i):
    te = 2.*np.pi*float(i/(framesEarth - 1.))
    tm = 2.*np.pi*float(i/(framesMoon - 1.))
    earth_x_marker = eEarth+(radEarthA*np.cos(te))
    earth_y_marker = radEarthP*np.sin(te)
    moon_x_marker = (earth_x_marker)+(radMoonA*np.cos(tm))
    moon_y_marker = (earth_y_marker)+(radMoonP*np.sin(tm))
    moon_xdata.append(moon_x_marker)
    moon_ydata.append(moon_y_marker)
    moonline.set_data(moon_xdata, moon_ydata) 
    return moonline,

animmoon = animation.FuncAnimation(fig, moonanimate, init_func=mooninit, frames=Nframes, interval=tinterval)
animoonline = animation.FuncAnimation(fig, moonlineanimate, init_func=moonlineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Moon----------------------------------------#
#----------------------------------------Earth----------------------------------------#





#----------------------------------------Mercury----------------------------------------#
circMercury = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radMercury, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circMercury)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Mercurycircle, = ax.plot([], [], marker='o', ms=2, color='grey')
Mercuryline, = ax.plot([], [], lw=1, color='brown')
Mercury_xdata = []
Mercury_ydata = []
MercuryC = radMercuryA+radMercuryP

#Mercury Animate
def Mercuryinit():
    Mercurycircle.set_data([], [])
    return Mercurycircle,
def Mercuryanimate(i):
    t = 2.*np.pi*float(i/(framesMercury - 1.))
    Mercury_x_marker = eMercury+(radMercuryA*np.cos(t))
    Mercury_y_marker = radMercuryP*np.sin(t)
    Mercurycircle.set_data(Mercury_x_marker, Mercury_y_marker)
    return Mercurycircle,
def Mercurylineinit():
	Mercuryline.set_data([], [])
	return Mercuryline,
def Mercurylineanimate(i):
	t = 2.*np.pi*float(i/(framesMercury - 1.))
	Mercury_x_marker = eMercury+(radMercuryA*np.cos(t))
	Mercury_y_marker = radMercuryP*np.sin(t)
	Mercury_xdata.append(Mercury_x_marker)
	Mercury_ydata.append(Mercury_y_marker)
	Mercuryline.set_data(Mercury_xdata, Mercury_ydata)
	return Mercuryline,
	
animMercury = animation.FuncAnimation(fig, Mercuryanimate, init_func=Mercuryinit, frames=framesMercury, interval=tinterval)
animMercuryline = animation.FuncAnimation(fig, Mercurylineanimate, init_func=Mercurylineinit, frames=framesMercury, interval=tinterval)
#----------------------------------------Mercury----------------------------------------#





#----------------------------------------Venus----------------------------------------#
circVenus = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radVenus, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circVenus)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Venuscircle, = ax.plot([], [], marker='o', ms=3, color='orange')
Venusline, = ax.plot([], [], lw=1, color='red')
Venus_xdata = []
Venus_ydata = []
VenusC = radVenusA+radVenusP

#Venus Animate
def Venusinit():
    Venuscircle.set_data([], [])
    return Venuscircle,
def Venusanimate(i):
    t = 2.*np.pi*float(i/(framesVenus - 1.))
    Venus_x_marker = eVenus+(radVenusA*np.cos(t))
    Venus_y_marker = radVenusP*np.sin(t)
    Venuscircle.set_data(Venus_x_marker, Venus_y_marker)
    return Venuscircle,
def Venuslineinit():
	Venusline.set_data([], [])
	return Venusline,
def Venuslineanimate(i):
	t = 2.*np.pi*float(i/(framesVenus - 1.))
	Venus_x_marker = eVenus+(radVenusA*np.cos(t))
	Venus_y_marker = radVenusP*np.sin(t)
	Venus_xdata.append(Venus_x_marker)
	Venus_ydata.append(Venus_y_marker)
	Venusline.set_data(Venus_xdata, Venus_ydata)
	return Venusline,
	
animVenus = animation.FuncAnimation(fig, Venusanimate, init_func=Venusinit, frames=framesVenus, interval=tinterval)
animVenusline = animation.FuncAnimation(fig, Venuslineanimate, init_func=Venuslineinit, frames=framesVenus, interval=tinterval)
#----------------------------------------Venus----------------------------------------#





#----------------------------------------Mars----------------------------------------#
circMars = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radMars, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circMars)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Marscircle, = ax.plot([], [], marker='o', ms=4, color='red')
Marsline, = ax.plot([], [], lw=1, color='orange')
Mars_xdata = []
Mars_ydata = []
MarsC = radMarsA+radMarsP

#Mars Animate
def Marsinit():
    Marscircle.set_data([], [])
    return Marscircle,
def Marsanimate(i):
    t = 2.*np.pi*float(i/(framesMars - 1.))
    Mars_x_marker = eMars+(radMarsA*np.cos(t))
    Mars_y_marker = radMarsP*np.sin(t)
    Marscircle.set_data(Mars_x_marker, Mars_y_marker)
    return Marscircle,
def Marslineinit():
	Marsline.set_data([], [])
	return Marsline,
def Marslineanimate(i):
	t = 2.*np.pi*float(i/(framesMars - 1.))
	Mars_x_marker = eMars+(radMarsA*np.cos(t))
	Mars_y_marker = radMarsP*np.sin(t)
	Mars_xdata.append(Mars_x_marker)
	Mars_ydata.append(Mars_y_marker)
	Marsline.set_data(Mars_xdata, Mars_ydata)
	return Marsline,
	
animMars = animation.FuncAnimation(fig, Marsanimate, init_func=Marsinit, frames=framesMars, interval=tinterval)
animMarsline = animation.FuncAnimation(fig, Marslineanimate, init_func=Marslineinit, frames=framesMars, interval=tinterval)


#----------------------------------------Phobos----------------------------------------#
Phoboscircle, = ax.plot([], [], marker='o', ms=1, color='red')
Phobosline, = ax.plot([], [], lw=1, color='0.75')
Phobos_xdata = []
Phobos_ydata = []

#Phobos Animate
def Phobosinit():
    Phoboscircle.set_data([], [])
    return Phoboscircle,

def Phobosanimate(i):
    te = 2.*np.pi*float(i/(framesMars - 1.))
    tm = 2.*np.pi*float(i/(framesPhobos - 1.))
    Mars_x_marker = eMars+(radMarsA*np.cos(te))
    Mars_y_marker = radMarsP*np.sin(te)
    Phobos_x_marker = (Mars_x_marker)+(radPhobosA*np.cos(tm))
    Phobos_y_marker = (Mars_y_marker)+(radPhobosP*np.sin(tm))
    Phoboscircle.set_data(Phobos_x_marker, Phobos_y_marker)
    return Phoboscircle,

def Phoboslineinit():
    Phobosline.set_data([], [])
    return Phobosline,

def Phoboslineanimate(i):
    te = 2.*np.pi*float(i/(framesMars - 1.))
    tm = 2.*np.pi*float(i/(framesPhobos - 1.))
    Mars_x_marker = eMars+(radMarsA*np.cos(te))
    Mars_y_marker = radMarsP*np.sin(te)
    Phobos_x_marker = (Mars_x_marker)+(radPhobosA*np.cos(tm))
    Phobos_y_marker = (Mars_y_marker)+(radPhobosP*np.sin(tm))
    Phobos_xdata.append(Phobos_x_marker)
    Phobos_ydata.append(Phobos_y_marker)
    Phobosline.set_data(Phobos_xdata, Phobos_ydata) 
    return Phobosline,

animPhobos = animation.FuncAnimation(fig, Phobosanimate, init_func=Phobosinit, frames=Nframes, interval=tinterval)
aniPhobosline = animation.FuncAnimation(fig, Phoboslineanimate, init_func=Phoboslineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Phobos----------------------------------------#


#----------------------------------------Deimos----------------------------------------#
Deimoscircle, = ax.plot([], [], marker='o', ms=1, color='red')
Deimosline, = ax.plot([], [], lw=1, color='0.75')
Deimos_xdata = []
Deimos_ydata = []

#Deimos Animate
def Deimosinit():
    Deimoscircle.set_data([], [])
    return Deimoscircle,

def Deimosanimate(i):
    te = 2.*np.pi*float(i/(framesMars - 1.))
    tm = 2.*np.pi*float(i/(framesDeimos - 1.))
    Mars_x_marker = eMars+(radMarsA*np.cos(te))
    Mars_y_marker = radMarsP*np.sin(te)
    Deimos_x_marker = (Mars_x_marker)+(radDeimosA*np.cos(tm))
    Deimos_y_marker = (Mars_y_marker)+(radDeimosP*np.sin(tm))
    Deimoscircle.set_data(Deimos_x_marker, Deimos_y_marker)
    return Deimoscircle,

def Deimoslineinit():
    Deimosline.set_data([], [])
    return Deimosline,

def Deimoslineanimate(i):
    te = 2.*np.pi*float(i/(framesMars - 1.))
    tm = 2.*np.pi*float(i/(framesDeimos - 1.))
    Mars_x_marker = eMars+(radMarsA*np.cos(te))
    Mars_y_marker = radMarsP*np.sin(te)
    Deimos_x_marker = (Mars_x_marker)+(radDeimosA*np.cos(tm))
    Deimos_y_marker = (Mars_y_marker)+(radDeimosP*np.sin(tm))
    Deimos_xdata.append(Deimos_x_marker)
    Deimos_ydata.append(Deimos_y_marker)
    Deimosline.set_data(Deimos_xdata, Deimos_ydata) 
    return Deimosline,

animDeimos = animation.FuncAnimation(fig, Deimosanimate, init_func=Deimosinit, frames=Nframes, interval=tinterval)
aniDeimosline = animation.FuncAnimation(fig, Deimoslineanimate, init_func=Deimoslineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Deimos----------------------------------------#
#----------------------------------------Mars----------------------------------------#





#----------------------------------------Vesta----------------------------------------#
circVesta = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radVesta, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circVesta)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Vestacircle, = ax.plot([], [], marker='o', ms=1, color='black')
Vestaline, = ax.plot([], [], lw=1, color='grey')
Vesta_xdata = []
Vesta_ydata = []
VestaC = radVestaA+radVestaP

#Vesta Animate
def Vestainit():
    Vestacircle.set_data([], [])
    return Vestacircle,
def Vestaanimate(i):
    t = 2.*np.pi*float(i/(framesVesta - 1.))
    Vesta_x_marker = eVesta+(radVestaA*np.cos(t))
    Vesta_y_marker = radVestaP*np.sin(t)
    Vestacircle.set_data(Vesta_x_marker, Vesta_y_marker)
    return Vestacircle,
def Vestalineinit():
	Vestaline.set_data([], [])
	return Vestaline,
def Vestalineanimate(i):
	t = 2.*np.pi*float(i/(framesVesta - 1.))
	Vesta_x_marker = eVesta+(radVestaA*np.cos(t))
	Vesta_y_marker = radVestaP*np.sin(t)
	Vesta_xdata.append(Vesta_x_marker)
	Vesta_ydata.append(Vesta_y_marker)
	Vestaline.set_data(Vesta_xdata, Vesta_ydata)
	return Vestaline,
	
animVesta = animation.FuncAnimation(fig, Vestaanimate, init_func=Vestainit, frames=framesVesta, interval=tinterval)
animVestaline = animation.FuncAnimation(fig, Vestalineanimate, init_func=Vestalineinit, frames=framesVesta, interval=tinterval)
#----------------------------------------Vesta----------------------------------------#





#----------------------------------------Ceres----------------------------------------#
circCeres = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radCeres, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circCeres)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Cerescircle, = ax.plot([], [], marker='o', ms=1, color='grey')
Ceresline, = ax.plot([], [], lw=1, color='black')
Ceres_xdata = []
Ceres_ydata = []
CeresC = radCeresA+radCeresP

#Ceres Animate
def Ceresinit():
    Cerescircle.set_data([], [])
    return Cerescircle,
def Ceresanimate(i):
    t = 2.*np.pi*float(i/(framesCeres - 1.))
    Ceres_x_marker = eCeres+(radCeresA*np.cos(t))
    Ceres_y_marker = radCeresP*np.sin(t)
    Cerescircle.set_data(Ceres_x_marker, Ceres_y_marker)
    return Cerescircle,
def Cereslineinit():
	Ceresline.set_data([], [])
	return Ceresline,
def Cereslineanimate(i):
	t = 2.*np.pi*float(i/(framesCeres - 1.))
	Ceres_x_marker = eCeres+(radCeresA*np.cos(t))
	Ceres_y_marker = radCeresP*np.sin(t)
	Ceres_xdata.append(Ceres_x_marker)
	Ceres_ydata.append(Ceres_y_marker)
	Ceresline.set_data(Ceres_xdata, Ceres_ydata)
	return Ceresline,
	
animCeres = animation.FuncAnimation(fig, Ceresanimate, init_func=Ceresinit, frames=framesCeres, interval=tinterval)
animCeresline = animation.FuncAnimation(fig, Cereslineanimate, init_func=Cereslineinit, frames=framesCeres, interval=tinterval)
#----------------------------------------Ceres----------------------------------------#





#----------------------------------------Jupiter----------------------------------------#
circJupiter = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radJupiter, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circJupiter)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Jupitercircle, = ax.plot([], [], marker='o', ms=6, color='red')
Jupiterline, = ax.plot([], [], lw=1, color='orange')
Jupiter_xdata = []
Jupiter_ydata = []
JupiterC = radJupiterA+radJupiterP

#Jupiter Animate
def Jupiterinit():
    Jupitercircle.set_data([], [])
    return Jupitercircle,
def Jupiteranimate(i):
    t = 2.*np.pi*float(i/(framesJupiter - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(t))
    Jupiter_y_marker = radJupiterP*np.sin(t)
    Jupitercircle.set_data(Jupiter_x_marker, Jupiter_y_marker)
    return Jupitercircle,
def Jupiterlineinit():
	Jupiterline.set_data([], [])
	return Jupiterline,
def Jupiterlineanimate(i):
	t = 2.*np.pi*float(i/(framesJupiter - 1.))
	Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(t))
	Jupiter_y_marker = radJupiterP*np.sin(t)
	Jupiter_xdata.append(Jupiter_x_marker)
	Jupiter_ydata.append(Jupiter_y_marker)
	Jupiterline.set_data(Jupiter_xdata, Jupiter_ydata)
	return Jupiterline,
	
animJupiter = animation.FuncAnimation(fig, Jupiteranimate, init_func=Jupiterinit, frames=framesJupiter, interval=tinterval)
animJupiterline = animation.FuncAnimation(fig, Jupiterlineanimate, init_func=Jupiterlineinit, frames=framesJupiter, interval=tinterval)



#----------------------------------------Io----------------------------------------#
Iocircle, = ax.plot([], [], marker='o', ms=1, color='red')
Ioline, = ax.plot([], [], lw=1, color='0.75')
Io_xdata = []
Io_ydata = []

#Io Animate
def Ioinit():
    Iocircle.set_data([], [])
    return Iocircle,

def Ioanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesIo - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Io_x_marker = (Jupiter_x_marker)+(radIoA*np.cos(tm))
    Io_y_marker = (Jupiter_y_marker)+(radIoP*np.sin(tm))
    Iocircle.set_data(Io_x_marker, Io_y_marker)
    return Iocircle,

def Iolineinit():
    Ioline.set_data([], [])
    return Ioline,

def Iolineanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesIo - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Io_x_marker = (Jupiter_x_marker)+(radIoA*np.cos(tm))
    Io_y_marker = (Jupiter_y_marker)+(radIoP*np.sin(tm))
    Io_xdata.append(Io_x_marker)
    Io_ydata.append(Io_y_marker)
    Ioline.set_data(Io_xdata, Io_ydata) 
    return Ioline,

animIo = animation.FuncAnimation(fig, Ioanimate, init_func=Ioinit, frames=Nframes, interval=tinterval)
aniIoline = animation.FuncAnimation(fig, Iolineanimate, init_func=Iolineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Io----------------------------------------#



#----------------------------------------Europa----------------------------------------#
Europacircle, = ax.plot([], [], marker='o', ms=1, color='red')
Europaline, = ax.plot([], [], lw=1, color='0.75')
Europa_xdata = []
Europa_ydata = []

#Europa Animate
def Europainit():
    Europacircle.set_data([], [])
    return Europacircle,

def Europaanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesEuropa - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Europa_x_marker = (Jupiter_x_marker)+(radEuropaA*np.cos(tm))
    Europa_y_marker = (Jupiter_y_marker)+(radEuropaP*np.sin(tm))
    Europacircle.set_data(Europa_x_marker, Europa_y_marker)
    return Europacircle,

def Europalineinit():
    Europaline.set_data([], [])
    return Europaline,

def Europalineanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesEuropa - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Europa_x_marker = (Jupiter_x_marker)+(radEuropaA*np.cos(tm))
    Europa_y_marker = (Jupiter_y_marker)+(radEuropaP*np.sin(tm))
    Europa_xdata.append(Europa_x_marker)
    Europa_ydata.append(Europa_y_marker)
    Europaline.set_data(Europa_xdata, Europa_ydata) 
    return Europaline,

animEuropa = animation.FuncAnimation(fig, Europaanimate, init_func=Europainit, frames=Nframes, interval=tinterval)
aniEuropaline = animation.FuncAnimation(fig, Europalineanimate, init_func=Europalineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Europa----------------------------------------#



#----------------------------------------Ganymede----------------------------------------#
Ganymedecircle, = ax.plot([], [], marker='o', ms=1, color='red')
Ganymedeline, = ax.plot([], [], lw=1, color='0.75')
Ganymede_xdata = []
Ganymede_ydata = []

#Ganymede Animate
def Ganymedeinit():
    Ganymedecircle.set_data([], [])
    return Ganymedecircle,

def Ganymedeanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesGanymede - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Ganymede_x_marker = (Jupiter_x_marker)+(radGanymedeA*np.cos(tm))
    Ganymede_y_marker = (Jupiter_y_marker)+(radGanymedeP*np.sin(tm))
    Ganymedecircle.set_data(Ganymede_x_marker, Ganymede_y_marker)
    return Ganymedecircle,

def Ganymedelineinit():
    Ganymedeline.set_data([], [])
    return Ganymedeline,

def Ganymedelineanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesGanymede - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Ganymede_x_marker = (Jupiter_x_marker)+(radGanymedeA*np.cos(tm))
    Ganymede_y_marker = (Jupiter_y_marker)+(radGanymedeP*np.sin(tm))
    Ganymede_xdata.append(Ganymede_x_marker)
    Ganymede_ydata.append(Ganymede_y_marker)
    Ganymedeline.set_data(Ganymede_xdata, Ganymede_ydata) 
    return Ganymedeline,

animGanymede = animation.FuncAnimation(fig, Ganymedeanimate, init_func=Ganymedeinit, frames=Nframes, interval=tinterval)
aniGanymedeline = animation.FuncAnimation(fig, Ganymedelineanimate, init_func=Ganymedelineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Ganymede----------------------------------------#



#----------------------------------------Callisto----------------------------------------#
Callistocircle, = ax.plot([], [], marker='o', ms=1, color='red')
Callistoline, = ax.plot([], [], lw=1, color='0.75')
Callisto_xdata = []
Callisto_ydata = []

#Callisto Animate
def Callistoinit():
    Callistocircle.set_data([], [])
    return Callistocircle,

def Callistoanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesCallisto - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Callisto_x_marker = (Jupiter_x_marker)+(radCallistoA*np.cos(tm))
    Callisto_y_marker = (Jupiter_y_marker)+(radCallistoP*np.sin(tm))
    Callistocircle.set_data(Callisto_x_marker, Callisto_y_marker)
    return Callistocircle,

def Callistolineinit():
    Callistoline.set_data([], [])
    return Callistoline,

def Callistolineanimate(i):
    te = 2.*np.pi*float(i/(framesJupiter - 1.))
    tm = 2.*np.pi*float(i/(framesCallisto - 1.))
    Jupiter_x_marker = eJupiter+(radJupiterA*np.cos(te))
    Jupiter_y_marker = radJupiterP*np.sin(te)
    Callisto_x_marker = (Jupiter_x_marker)+(radCallistoA*np.cos(tm))
    Callisto_y_marker = (Jupiter_y_marker)+(radCallistoP*np.sin(tm))
    Callisto_xdata.append(Callisto_x_marker)
    Callisto_ydata.append(Callisto_y_marker)
    Callistoline.set_data(Callisto_xdata, Callisto_ydata) 
    return Callistoline,

animCallisto = animation.FuncAnimation(fig, Callistoanimate, init_func=Callistoinit, frames=Nframes, interval=tinterval)
aniCallistoline = animation.FuncAnimation(fig, Callistolineanimate, init_func=Callistolineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Callisto----------------------------------------#
#----------------------------------------Jupiter----------------------------------------#





#----------------------------------------Saturn----------------------------------------#
circSaturn = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radSaturn, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circSaturn)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Saturncircle, = ax.plot([], [], marker='o', ms=5, color='orange')
Saturnline, = ax.plot([], [], lw=1, color='red')
Saturn_xdata = []
Saturn_ydata = []
SaturnC = radSaturnA+radSaturnP

#Saturn Animate
def Saturninit():
    Saturncircle.set_data([], [])
    return Saturncircle,
def Saturnanimate(i):
    t = 2.*np.pi*float(i/(framesSaturn - 1.))
    Saturn_x_marker = eSaturn+(radSaturnA*np.cos(t))
    Saturn_y_marker = radSaturnP*np.sin(t)
    Saturncircle.set_data(Saturn_x_marker, Saturn_y_marker)
    return Saturncircle,
def Saturnlineinit():
	Saturnline.set_data([], [])
	return Saturnline,
def Saturnlineanimate(i):
	t = 2.*np.pi*float(i/(framesSaturn - 1.))
	Saturn_x_marker = eSaturn+(radSaturnA*np.cos(t))
	Saturn_y_marker = radSaturnP*np.sin(t)
	Saturn_xdata.append(Saturn_x_marker)
	Saturn_ydata.append(Saturn_y_marker)
	Saturnline.set_data(Saturn_xdata, Saturn_ydata)
	return Saturnline,
	
animSaturn = animation.FuncAnimation(fig, Saturnanimate, init_func=Saturninit, frames=framesSaturn, interval=tinterval)
animSaturnline = animation.FuncAnimation(fig, Saturnlineanimate, init_func=Saturnlineinit, frames=framesSaturn, interval=tinterval)



#----------------------------------------Titan----------------------------------------#
Titancircle, = ax.plot([], [], marker='o', ms=3, color='red')
Titanline, = ax.plot([], [], lw=1, color='orange')
Titan_xdata = []
Titan_ydata = []

#Titan Animate
def Titaninit():
    Titancircle.set_data([], [])
    return Titancircle,

def Titananimate(i):
    te = 2.*np.pi*float(i/(framesSaturn - 1.))
    tm = 2.*np.pi*float(i/(framesTitan - 1.))
    Saturn_x_marker = eSaturn+(radSaturnA*np.cos(te))
    Saturn_y_marker = radSaturnP*np.sin(te)
    Titan_x_marker = (Saturn_x_marker)+(radTitanA*np.cos(tm))
    Titan_y_marker = (Saturn_y_marker)+(radTitanP*np.sin(tm))
    Titancircle.set_data(Titan_x_marker, Titan_y_marker)
    return Titancircle,

def Titanlineinit():
    Titanline.set_data([], [])
    return Titanline,

def Titanlineanimate(i):
    te = 2.*np.pi*float(i/(framesSaturn - 1.))
    tm = 2.*np.pi*float(i/(framesTitan - 1.))
    Saturn_x_marker = eSaturn+(radSaturnA*np.cos(te))
    Saturn_y_marker = radSaturnP*np.sin(te)
    Titan_x_marker = (Saturn_x_marker)+(radTitanA*np.cos(tm))
    Titan_y_marker = (Saturn_y_marker)+(radTitanP*np.sin(tm))
    Titan_xdata.append(Titan_x_marker)
    Titan_ydata.append(Titan_y_marker)
    Titanline.set_data(Titan_xdata, Titan_ydata) 
    return Titanline,

animTitan = animation.FuncAnimation(fig, Titananimate, init_func=Titaninit, frames=Nframes, interval=tinterval)
aniTitanline = animation.FuncAnimation(fig, Titanlineanimate, init_func=Titanlineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Titan----------------------------------------#


#----------------------------------------Enceladus----------------------------------------#
Enceladuscircle, = ax.plot([], [], marker='o', ms=1, color='cyan')
Enceladusline, = ax.plot([], [], lw=1, color='blue')
Enceladus_xdata = []
Enceladus_ydata = []

#Enceladus Animate
def Enceladusinit():
    Enceladuscircle.set_data([], [])
    return Enceladuscircle,

def Enceladusanimate(i):
    te = 2.*np.pi*float(i/(framesSaturn - 1.))
    tm = 2.*np.pi*float(i/(framesEnceladus - 1.))
    Saturn_x_marker = eSaturn+(radSaturnA*np.cos(te))
    Saturn_y_marker = radSaturnP*np.sin(te)
    Enceladus_x_marker = (Saturn_x_marker)+(radEnceladusA*np.cos(tm))
    Enceladus_y_marker = (Saturn_y_marker)+(radEnceladusP*np.sin(tm))
    Enceladuscircle.set_data(Enceladus_x_marker, Enceladus_y_marker)
    return Enceladuscircle,

def Enceladuslineinit():
    Enceladusline.set_data([], [])
    return Enceladusline,

def Enceladuslineanimate(i):
    te = 2.*np.pi*float(i/(framesSaturn - 1.))
    tm = 2.*np.pi*float(i/(framesEnceladus - 1.))
    Saturn_x_marker = eSaturn+(radSaturnA*np.cos(te))
    Saturn_y_marker = radSaturnP*np.sin(te)
    Enceladus_x_marker = (Saturn_x_marker)+(radEnceladusA*np.cos(tm))
    Enceladus_y_marker = (Saturn_y_marker)+(radEnceladusP*np.sin(tm))
    Enceladus_xdata.append(Enceladus_x_marker)
    Enceladus_ydata.append(Enceladus_y_marker)
    Enceladusline.set_data(Enceladus_xdata, Enceladus_ydata) 
    return Enceladusline,

animEnceladus = animation.FuncAnimation(fig, Enceladusanimate, init_func=Enceladusinit, frames=Nframes, interval=tinterval)
aniEnceladusline = animation.FuncAnimation(fig, Enceladuslineanimate, init_func=Enceladuslineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Enceladus----------------------------------------#
#----------------------------------------Saturn----------------------------------------#





#----------------------------------------Uranus----------------------------------------#
circUranus = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radUranus, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circUranus)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Uranuscircle, = ax.plot([], [], marker='o', ms=2, color='cyan')
Uranusline, = ax.plot([], [], lw=1, color='blue')
Uranus_xdata = []
Uranus_ydata = []
UranusC = radUranusA+radUranusP

#Uranus Animate
def Uranusinit():
    Uranuscircle.set_data([], [])
    return Uranuscircle,
def Uranusanimate(i):
    t = 2.*np.pi*float(i/(framesUranus - 1.))
    Uranus_x_marker = eUranus+(radUranusA*np.cos(t))
    Uranus_y_marker = radUranusP*np.sin(t)
    Uranuscircle.set_data(Uranus_x_marker, Uranus_y_marker)
    return Uranuscircle,
def Uranuslineinit():
	Uranusline.set_data([], [])
	return Uranusline,
def Uranuslineanimate(i):
	t = 2.*np.pi*float(i/(framesUranus - 1.))
	Uranus_x_marker = eUranus+(radUranusA*np.cos(t))
	Uranus_y_marker = radUranusP*np.sin(t)
	Uranus_xdata.append(Uranus_x_marker)
	Uranus_ydata.append(Uranus_y_marker)
	Uranusline.set_data(Uranus_xdata, Uranus_ydata)
	return Uranusline,
	
animUranus = animation.FuncAnimation(fig, Uranusanimate, init_func=Uranusinit, frames=framesUranus, interval=tinterval)
animUranusline = animation.FuncAnimation(fig, Uranuslineanimate, init_func=Uranuslineinit, frames=framesUranus, interval=tinterval)



#----------------------------------------Miranda----------------------------------------#
Mirandacircle, = ax.plot([], [], marker='o', ms=1, color='grey')
Mirandaline, = ax.plot([], [], lw=1, color='0.75')
Miranda_xdata = []
Miranda_ydata = []

#Miranda Animate
def Mirandainit():
    Mirandacircle.set_data([], [])
    return Mirandacircle,

def Mirandaanimate(i):
    te = 2.*np.pi*float(i/(framesUranus - 1.))
    tm = 2.*np.pi*float(i/(framesMiranda - 1.))
    Uranus_x_marker = eUranus+(radUranusA*np.cos(te))
    Uranus_y_marker = radUranusP*np.sin(te)
    Miranda_x_marker = (Uranus_x_marker)+(radMirandaA*np.cos(tm))
    Miranda_y_marker = (Uranus_y_marker)+(radMirandaP*np.sin(tm))
    Mirandacircle.set_data(Miranda_x_marker, Miranda_y_marker)
    return Mirandacircle,

def Mirandalineinit():
    Mirandaline.set_data([], [])
    return Mirandaline,

def Mirandalineanimate(i):
    te = 2.*np.pi*float(i/(framesUranus - 1.))
    tm = 2.*np.pi*float(i/(framesMiranda - 1.))
    Uranus_x_marker = eUranus+(radUranusA*np.cos(te))
    Uranus_y_marker = radUranusP*np.sin(te)
    Miranda_x_marker = (Uranus_x_marker)+(radMirandaA*np.cos(tm))
    Miranda_y_marker = (Uranus_y_marker)+(radMirandaP*np.sin(tm))
    Miranda_xdata.append(Miranda_x_marker)
    Miranda_ydata.append(Miranda_y_marker)
    Mirandaline.set_data(Miranda_xdata, Miranda_ydata) 
    return Mirandaline,

animMiranda = animation.FuncAnimation(fig, Mirandaanimate, init_func=Mirandainit, frames=Nframes, interval=tinterval)
aniMirandaline = animation.FuncAnimation(fig, Mirandalineanimate, init_func=Mirandalineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Miranda----------------------------------------#
#----------------------------------------Uranus----------------------------------------#





#----------------------------------------Neptune----------------------------------------#
circNeptune = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radNeptune, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circNeptune)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Neptunecircle, = ax.plot([], [], marker='o', ms=2, color='blue')
Neptuneline, = ax.plot([], [], lw=1, color='cyan')
Neptune_xdata = []
Neptune_ydata = []
NeptuneC = radNeptuneA+radNeptuneP

#Neptune Animate
def Neptuneinit():
    Neptunecircle.set_data([], [])
    return Neptunecircle,
def Neptuneanimate(i):
    t = 2.*np.pi*float(i/(framesNeptune - 1.))
    Neptune_x_marker = eNeptune+(radNeptuneA*np.cos(t))
    Neptune_y_marker = radNeptuneP*np.sin(t)
    Neptunecircle.set_data(Neptune_x_marker, Neptune_y_marker)
    return Neptunecircle,
def Neptunelineinit():
	Neptuneline.set_data([], [])
	return Neptuneline,
def Neptunelineanimate(i):
	t = 2.*np.pi*float(i/(framesNeptune - 1.))
	Neptune_x_marker = eNeptune+(radNeptuneA*np.cos(t))
	Neptune_y_marker = radNeptuneP*np.sin(t)
	Neptune_xdata.append(Neptune_x_marker)
	Neptune_ydata.append(Neptune_y_marker)
	Neptuneline.set_data(Neptune_xdata, Neptune_ydata)
	return Neptuneline,
	
animNeptune = animation.FuncAnimation(fig, Neptuneanimate, init_func=Neptuneinit, frames=framesNeptune, interval=tinterval)
animNeptuneline = animation.FuncAnimation(fig, Neptunelineanimate, init_func=Neptunelineinit, frames=framesNeptune, interval=tinterval)



#----------------------------------------Triton----------------------------------------#
Tritoncircle, = ax.plot([], [], marker='o', ms=1, color='red')
Tritonline, = ax.plot([], [], lw=1, color='0.75')
Triton_xdata = []
Triton_ydata = []

#Triton Animate
def Tritoninit():
    Tritoncircle.set_data([], [])
    return Tritoncircle,

def Tritonanimate(i):
    te = 2.*np.pi*float(i/(framesNeptune - 1.))
    tm = 2.*np.pi*float(i/(framesTriton - 1.))
    Neptune_x_marker = eNeptune+(radNeptuneA*np.cos(te))
    Neptune_y_marker = radNeptuneP*np.sin(te)
    Triton_x_marker = (Neptune_x_marker)+(radTritonA*np.cos(tm))
    Triton_y_marker = (Neptune_y_marker)+(radTritonP*np.sin(tm))
    Tritoncircle.set_data(Triton_x_marker, Triton_y_marker)
    return Tritoncircle,

def Tritonlineinit():
    Tritonline.set_data([], [])
    return Tritonline,

def Tritonlineanimate(i):
    te = 2.*np.pi*float(i/(framesNeptune - 1.))
    tm = 2.*np.pi*float(i/(framesTriton - 1.))
    Neptune_x_marker = eNeptune+(radNeptuneA*np.cos(te))
    Neptune_y_marker = radNeptuneP*np.sin(te)
    Triton_x_marker = (Neptune_x_marker)+(radTritonA*np.cos(tm))
    Triton_y_marker = (Neptune_y_marker)+(radTritonP*np.sin(tm))
    Triton_xdata.append(Triton_x_marker)
    Triton_ydata.append(Triton_y_marker)
    Tritonline.set_data(Triton_xdata, Triton_ydata) 
    return Tritonline,

animTriton = animation.FuncAnimation(fig, Tritonanimate, init_func=Tritoninit, frames=Nframes, interval=tinterval)
aniTritonline = animation.FuncAnimation(fig, Tritonlineanimate, init_func=Tritonlineinit, frames=Nframes, interval=tinterval)
#----------------------------------------Triton----------------------------------------#
#----------------------------------------Neptune----------------------------------------#





#----------------------------------------Pluto----------------------------------------#
circPluto = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radPluto, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circPluto)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Plutocircle, = ax.plot([], [], marker='o', ms=1, color='brown')
Plutoline, = ax.plot([], [], lw=1, color='black')
Pluto_xdata = []
Pluto_ydata = []
PlutoC = radPlutoA+radPlutoP

#Pluto Animate
def Plutoinit():
    Plutocircle.set_data([], [])
    return Plutocircle,
def Plutoanimate(i):
    t = 2.*np.pi*float(i/(framesPluto - 1.))
    Pluto_x_marker = ePluto+(radPlutoA*np.cos(t))
    Pluto_y_marker = radPlutoP*np.sin(t)
    Plutocircle.set_data(Pluto_x_marker, Pluto_y_marker)
    return Plutocircle,
def Plutolineinit():
	Plutoline.set_data([], [])
	return Plutoline,
def Plutolineanimate(i):
	t = 2.*np.pi*float(i/(framesPluto - 1.))
	Pluto_x_marker = ePluto+(radPlutoA*np.cos(t))
	Pluto_y_marker = radPlutoP*np.sin(t)
	Pluto_xdata.append(Pluto_x_marker)
	Pluto_ydata.append(Pluto_y_marker)
	Plutoline.set_data(Pluto_xdata, Pluto_ydata)
	return Plutoline,
	
animPluto = animation.FuncAnimation(fig, Plutoanimate, init_func=Plutoinit, frames=framesPluto, interval=tinterval)
animPlutoline = animation.FuncAnimation(fig, Plutolineanimate, init_func=Plutolineinit, frames=framesPluto, interval=tinterval)
#----------------------------------------Pluto----------------------------------------#





#----------------------------------------Haumea----------------------------------------#
circHaumea = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radHaumea, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circHaumea)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Haumeacircle, = ax.plot([], [], marker='o', ms=2, color='black')
Haumealine, = ax.plot([], [], lw=1, color='grey')
Haumea_xdata = []
Haumea_ydata = []
HaumeaC = radHaumeaA+radHaumeaP

#Haumea Animate
def Haumeainit():
    Haumeacircle.set_data([], [])
    return Haumeacircle,
def Haumeaanimate(i):
    t = 2.*np.pi*float(i/(framesHaumea - 1.))
    Haumea_x_marker = eHaumea+(radHaumeaA*np.cos(t))
    Haumea_y_marker = radHaumeaP*np.sin(t)
    Haumeacircle.set_data(Haumea_x_marker, Haumea_y_marker)
    return Haumeacircle,
def Haumealineinit():
	Haumealine.set_data([], [])
	return Haumealine,
def Haumealineanimate(i):
	t = 2.*np.pi*float(i/(framesHaumea - 1.))
	Haumea_x_marker = eHaumea+(radHaumeaA*np.cos(t))
	Haumea_y_marker = radHaumeaP*np.sin(t)
	Haumea_xdata.append(Haumea_x_marker)
	Haumea_ydata.append(Haumea_y_marker)
	Haumealine.set_data(Haumea_xdata, Haumea_ydata)
	return Haumealine,
	
animHaumea = animation.FuncAnimation(fig, Haumeaanimate, init_func=Haumeainit, frames=framesHaumea, interval=tinterval)
animHaumealine = animation.FuncAnimation(fig, Haumealineanimate, init_func=Haumealineinit, frames=framesHaumea, interval=tinterval)
#----------------------------------------Haumea----------------------------------------#





#----------------------------------------Makemake----------------------------------------#
circMakemake = plt.Circle((0,0), radius=rad, facecolor="None", edgecolor="k", lw=1)
circ= plt.Circle((0,0), radius=radMakemake, facecolor="None", edgecolor="k", lw=1)
ax.add_patch(circMakemake)
ax.add_patch(circ)
ax.grid(False)
ax.axis('off')
Makemakecircle, = ax.plot([], [], marker='o', ms=2, color='grey')
Makemakeline, = ax.plot([], [], lw=1, color='black')
Makemake_xdata = []
Makemake_ydata = []
MakemakeC = radMakemakeA+radMakemakeP

#Makemake Animate
def Makemakeinit():
    Makemakecircle.set_data([], [])
    return Makemakecircle,
def Makemakeanimate(i):
    t = 2.*np.pi*float(i/(framesMakemake - 1.))
    Makemake_x_marker = eMakemake+(radMakemakeA*np.cos(t))
    Makemake_y_marker = radMakemakeP*np.sin(t)
    Makemakecircle.set_data(Makemake_x_marker, Makemake_y_marker)
    return Makemakecircle,
def Makemakelineinit():
	Makemakeline.set_data([], [])
	return Makemakeline,
def Makemakelineanimate(i):
	t = 2.*np.pi*float(i/(framesMakemake - 1.))
	Makemake_x_marker = eMakemake+(radMakemakeA*np.cos(t))
	Makemake_y_marker = radMakemakeP*np.sin(t)
	Makemake_xdata.append(Makemake_x_marker)
	Makemake_ydata.append(Makemake_y_marker)
	Makemakeline.set_data(Makemake_xdata, Makemake_ydata)
	return Makemakeline,
	
animMakemake = animation.FuncAnimation(fig, Makemakeanimate, init_func=Makemakeinit, frames=framesMakemake, interval=tinterval)
animMakemakeline = animation.FuncAnimation(fig, Makemakelineanimate, init_func=Makemakelineinit, frames=framesMakemake, interval=tinterval)
#----------------------------------------Makemake----------------------------------------#





#----------------------------------------Halleys----------------------------------------#
Halleyscircle, = ax.plot([], [], marker='o', ms=4, color='blue')
Halleysline, = ax.plot([], [], lw=1, color='blue')
Halleys_xdata = []
Halleys_ydata = []
HalleysC = radHalleysA+radHalleysP

#Halleys Animate
def Halleysinit():
    Halleyscircle.set_data([], [])
    return Halleyscircle,
def Halleysanimate(i):
    t = 2.*np.pi*float(i/(framesHalleys - 1.))
    Halleys_x_marker = eHalleys+(radHalleysA*np.cos(t))
    Halleys_y_marker = radHalleysP*np.sin(t)
    Halleyscircle.set_data(Halleys_x_marker, Halleys_y_marker)
    return Halleyscircle,
def Halleyslineinit():
	Halleysline.set_data([], [])
	return Halleysline,
def Halleyslineanimate(i):
	t = 2.*np.pi*float(i/(framesHalleys - 1.))
	Halleys_x_marker = eHalleys+(radHalleysA*np.cos(t))
	Halleys_y_marker = radHalleysP*np.sin(t)
	Halleys_xdata.append(Halleys_x_marker)
	Halleys_ydata.append(Halleys_y_marker)
	Halleysline.set_data(Halleys_xdata, Halleys_ydata)
	return Halleysline,
	
animHalleys = animation.FuncAnimation(fig, Halleysanimate, init_func=Halleysinit, frames=framesHalleys, interval=tinterval)
animHalleysline = animation.FuncAnimation(fig, Halleyslineanimate, init_func=Halleyslineinit, frames=framesHalleys, interval=tinterval)
#----------------------------------------Halleys----------------------------------------#











#Animation call (blit=True means only re-draw parts with changes)
#anim = animation.FuncAnimation((fig, earthanimate, init_func=earthinit, frames=Nframes, interval=20, blit=True,(fig, sunanimate, init_func=suninit, frames=Nframes, interval=20, blit=True)
#anim = animation.FuncAnimation(fig, (earthanimate, sunanimate), init_func=(earthinit, suninit), frames=Nframes, interval=20, blit=True)





plt.show()
