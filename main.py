from kivymd.app import MDApp

from kivy.core.window import Window
from kivymd.uix.chip import MDChip
from kivymd.uix.slider import MDSlider
from kivymd.uix.selectioncontrol import MDCheckbox

from kivymd.uix.carousel import MDCarousel

from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton, MDFillRoundFlatIconButton
from kivy.uix.button import Button

from kivymd.uix.label import MDLabel, MDIcon

from kivy.animation import AnimationTransition, Animation

from kivy.uix.screenmanager import ScreenManager, FadeTransition

from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

from kivymd.uix.screen import MDScreen

from kivymd.uix.button import MDRaisedButton, MDIconButton

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.uix.card import MDCard
from kivymd.theming import ThemableBehavior


from kivy.clock import Clock

from threading import Timer
import time
from random import uniform, choice
import sqlite3

__version__ = '2.1.0'


int2word = {1.0: 'one', 2.0: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

red = (0.77, 0.47, 0.47, 1)
red_light = (0.9, 0.5, 0.5, 0.3)

green = (0.47, 0.77, 0.47, 1)

yellow = (0.74, 0.77, 0.47, 1)
yellow_light = (0.98, 0.90, 0.098, 1)

optional1 = (0.75, 0.75, 0.75, 0.9)

optional2 = (0.8, 0.7, 0.7, 0.9)

optional3 = (0.85, 0.75, 0.75, 0.9)

optional4 = (0.9, 0.8, 0.8, 0.9)

optional5 = (0.8, 0.85, 0.85, 0.95)

center = {'center_x': .5, 'center_y': .5}


class MainMenu(ThemableBehavior, MDFloatLayout, MDScreen):

	def __init__(self, **kwargs):

		super().__init__(**kwargs)

		self.md_bg_color = self.theme_cls.primary_light

		self.size = Window.size

		self.card = MDCard(size_hint = (0.5, 0.7),
			radius = (15, 5, 15, 5),
			pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			md_bg_color = self.theme_cls.primary_color,
			elevation = 15,
			opacity = 0)

		self.add_widget(self.card)

		self.cardLayout = MDFloatLayout(size = self.card.size)
		self.card.add_widget(self.cardLayout)

		self.titleLabel = MDLabel(text = 'React',
			font_style = 'H3',
			halign = 'center',
			pos_hint = {"center_x": .5, "center_y": .8},
			opacity = 0)
		self.cardLayout.add_widget(self.titleLabel)

		self.modesButton = MDIconButton(icon = 'play-circle',
			pos_hint = {'center_x': 0.33, 'center_y': 0.56},
			user_font_size = 48,
			md_bg_color = self.theme_cls.accent_light)
		self.modesButton.bind(on_press = lambda event, x='Modes': self.loadScreen(screenType = x))
		self.cardLayout.add_widget(self.modesButton)

		self.profileButton = MDIconButton(icon = 'account',
			pos_hint = {'center_x': 0.66, 'center_y': 0.56},
			user_font_size = 48,
			md_bg_color = self.theme_cls.accent_light)
		self.profileButton.bind(on_press = lambda event, x='Statistics': self.loadScreen(screenType = x))
		self.cardLayout.add_widget(self.profileButton)

		self.leaderboardButton = MDIconButton(icon = 'podium-gold',
			pos_hint = {'center_x': 0.33, 'center_y': 0.23},
			user_font_size = 48,
			md_bg_color = self.theme_cls.accent_light)
		self.cardLayout.add_widget(self.leaderboardButton)
		
		self.settingsButton = MDIconButton(icon = 'cogs',
			pos_hint = {'center_x': 0.66, 'center_y': 0.23},
			user_font_size = 48,
			md_bg_color = self.theme_cls.accent_light)
		self.cardLayout.add_widget(self.settingsButton)
		self.settingsButton.bind(on_press = self.settingsLoad)
		
		cardAnim = Animation(opacity = 1, duration = 1.5)

		cardAnim.start(self.card)

		cardAnim.bind(on_complete = lambda anim, card: anim.start(self.titleLabel))

	def loadScreen(self, screenType):

		self.manager.current = str(screenType)

	def settingsLoad(self, event):
		self.makeSettingCard()

		fadeOut = Animation(opacity = 0, d = 1)
		fadeIn = Animation(opacity = 1, d = 1)

		fadeOut.start(self.card)
		fadeOut.bind(on_complete = lambda event, instance: fadeIn.start(self.settingsCard))
		fadeOut.bind(on_complete = lambda event, instance: self.remove_widget(self.card))
	
	def settingsFade(self, event):

		fadeOut = Animation(opacity = 0, d = 1)
		fadeIn = Animation(opacity = 1, d = 1)

		self.add_widget(self.card)
		self.card.opacity = 0

		fadeOut.start(self.settingsCard)

		fadeOut.bind(on_complete = lambda anim, instance: fadeIn.start(self.card))
		fadeOut.bind(on_complete = lambda anim, instance: self.remove_widget(self.settingsCard))

	def makeSettingCard(self):

		self.settingsCard = MDCard(size_hint = (0.5, 0.7),
			radius = (15, 5, 15, 5),
			pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			md_bg_color = self.theme_cls.primary_color,
			elevation = 15,
			opacity = 0)
		self.add_widget(self.settingsCard)

		self.cardLayout = MDFloatLayout(size = self.settingsCard.size)
		self.settingsCard.add_widget(self.cardLayout)

		title = MDLabel(text = 'Settings',
		pos_hint = {'center_x': .5, 'center_y': .9},
		halign = 'center',
		font_style = 'H3')
		self.cardLayout.add_widget(title)

		returnButton = MDIconButton(icon = 'arrow-left',
		pos_hint = {'center_x': .5, 'center_y': .075},
		on_press = self.settingsFade)

		self.cardLayout.add_widget(returnButton)


		self.makeColorCard()
		self.makeAboutCard()

	def makeAboutCard(self):

		self.aboutCard = MDCard(radius = 15,
		pos_hint = {'center_x': 0.5, 'center_y': 0.3},
		size_hint = (0.9, 0.3),
		md_bg_color = self.theme_cls.primary_light,
		elevation = 15,
		ripple_behavior = True,
		on_release = lambda event: print('about clicked'))
		self.cardLayout.add_widget(self.aboutCard)

		aboutLabel = MDLabel(text = 'About',
		halign = 'center',
		valign = 'center',
		pos_hint = center,
		font_style = 'Body1')

		self.aboutCard.add_widget(aboutLabel)

	def makeColorCard(self):

		global yellow
		global red
		global green

		self.colorCard = MDCard(radius = 15,
		pos_hint = {'center_x': 0.5, 'center_y': 0.65},
		size_hint = (0.9, 0.3),
		md_bg_color = self.theme_cls.primary_light,
		elevation = 15)
		self.cardLayout.add_widget(self.colorCard)

		layout = MDFloatLayout(size = self.colorCard.size)
		self.colorCard.add_widget(layout)

		self.greenButton = MDRaisedButton(md_bg_color = green,
		pos_hint = {'center_x': .5, 'center_y': .5},
		size_hint = (0.25, 0.75))
		layout.add_widget(self.greenButton)
		self.greenButton.bind(on_press = lambda instance: self.changeTheme(button = 'Green'))

		self.yellowButton = MDRaisedButton(md_bg_color = yellow,
		pos_hint = {'center_x': .2, 'center_y': .5},
		size_hint = (0.25, 0.75))
		layout.add_widget(self.yellowButton)

		self.yellowButton.bind(on_press = lambda instance: self.changeTheme(button = 'Yellow'))

		self.redButton = MDRaisedButton(md_bg_color = red,
		pos_hint = {'center_x': .8, 'center_y': .5},
		size_hint = (0.25, 0.75))
		layout.add_widget(self.redButton)
		self.redButton.bind(on_press = lambda instance: self.changeTheme(button = 'Red'))

	def changeTheme(self, button):

		self.theme_cls.primary_palette = button

		if button == 'Green':
			self.theme_cls.accent_palette = 'Purple'
			ModeScreen().changeTheme(button = 'Green')

		elif button == 'Yellow':
			self.theme_cls.accent_palette = 'Blue'
			ModeScreen().changeTheme(button = 'Yellow')

		elif button == 'Red':
			ModeScreen().changeTheme(button = 'Red')
			self.theme_cls.accent_palette = 'Cyan'
		
		self.md_bg_color = self.theme_cls.primary_light

		self.card.md_bg_color = self.theme_cls.primary_color
		self.settingsCard.md_bg_color = self.theme_cls.primary_color

		self.colorCard.md_bg_color = self.theme_cls.primary_light
		self.aboutCard.md_bg_color = self.theme_cls.primary_light

		self.modesButton.md_bg_color = self.theme_cls.accent_light
		self.profileButton.md_bg_color = self.theme_cls.accent_light
		self.settingsButton.md_bg_color = self.theme_cls.accent_light
		self.leaderboardButton.md_bg_color = self.theme_cls.accent_light

		self.greenButton.md_bg_color = green
		self.yellowButton.md_bg_color = yellow
		self.redButton.md_bg_color = red

class ModeScreen(ThemableBehavior, MDFloatLayout, MDScreen):

	def __init__(self, **kwargs):

		super().__init__(**kwargs)

		self.size = Window.size

		self.makeTimeframeCard()
		self.makeSetCard()
		self.makeTrafficCard()

		self.returnButton = MDFloatingActionButton(icon = 'arrow-left',
		pos_hint = {'center_x': .075, 'center_y': .925},
		user_font_size = 48,
		radius = 64,
		md_bg_color = self.theme_cls.accent_color)
		self.returnButton.bind(on_press = lambda event: self.loadScreen(screenType='Menu'))

		self.add_widget(self.returnButton)

	def loadScreen(self, screenType):

		self.manager.current = str(screenType)

	def on_pre_enter(self):
		
		Clock.schedule_once(self.changeTheme)

	def changeTheme(self, button):

		# anim = Animation(opacity = 1, d = 0.5)
		# anim.start(self)

		if button == 'Green':
			self.theme_cls.primary_palette = 'Green'
			self.theme_cls.accent_palette = 'Purple'

		elif button == 'Yellow':
			self.theme_cls.primary_palette = 'Yellow'
			self.theme_cls.accent_palette = 'Blue'

		elif button == 'Red':
			self.theme_cls.primary_palette = 'Red'
			self.theme_cls.accent_palette = 'Cyan'

		self.md_bg_color = self.theme_cls.primary_light

		self.timeFrameCard.md_bg_color = self.theme_cls.primary_color
		self.setCard.md_bg_color = self.theme_cls.primary_light
		self.trafficCard.md_bg_color = self.theme_cls.primary_light

		self.returnButton.md_bg_color = self.theme_cls.accent_color

	def makeTimeframeCard(self):

		self.timeFrameCard = MDCard(size_hint = (0.9, 0.45),
			pos_hint = {'center_x': .5, 'center_y': .735},
			radius = (30, 30, 5, 5),
			md_bg_color = self.theme_cls.primary_color,
			elevation = 8,
			ripple_behavior = True,
			on_release = lambda event, x='Time Frame': self.loadScreen(screenType = x))

		self.add_widget(self.timeFrameCard)

		# Layout for the card

		layout = MDFloatLayout(size = self.timeFrameCard.size)

		self.timeFrameCard.add_widget(layout)

		icon = MDIconButton(icon = 'flash',
			pos_hint = {'center_x': 0.5, 'center_y': 0.6})



		layout.add_widget(icon)


		label = MDLabel(text = 'Time Frame',
			pos_hint = {'x': 0, 'y': -0.1},
			halign = 'center',
			font_style = 'Body1')

		descLabel = MDLabel(text = 'React within a set timeframe to gain a streak.',
			pos_hint = {'x': 0, 'y': -0.18},
			halign = 'center',
			font_style = 'Caption')

		layout.add_widget(label)
		layout.add_widget(descLabel)

	def makeSetCard(self):

		# Card for content

		self.setCard = MDCard(size_hint = (0.44, 0.45),
			pos_hint = {'center_x': .27, 'center_y': .27},
			radius = (5, 5, 5, 30),
			md_bg_color = self.theme_cls.primary_light,
			elevation = 8,
			ripple_behavior = True,
			on_release = lambda event, x='Set': self.loadScreen(screenType = x))

		self.add_widget(self.setCard)

		# Layout for the card

		layout = MDFloatLayout(size = self.setCard.size)

		self.setCard.add_widget(layout)

		icon = MDIconButton(icon = 'av-timer',
			pos_hint = {'center_x': 0.5, 'center_y': 0.6})

		layout.add_widget(icon)

		label = MDLabel(text = 'Free Mode',
			pos_hint = {'x': 0, 'y': -0.1},
			halign = 'center',
			font_style = 'Body1')

		descLabel = MDLabel(text = 'Take as long as you like to react.',
		halign = 'center',
		font_style = 'Caption',
		pos_hint = {'x': 0, 'y': -0.18})

		layout.add_widget(label)
		layout.add_widget(descLabel)

	def makeTrafficCard(self):

		self.trafficCard = MDCard(size_hint = (0.45, 0.45),
			pos_hint = {'center_x': .725, 'center_y': .27},
			radius = (5, 5, 30, 5),
			md_bg_color = self.theme_cls.primary_light,
			elevation = 8,
			ripple_behavior = True,
			on_release = lambda event, x='Traffic': self.loadScreen(screenType = x))

		self.add_widget(self.trafficCard)

		# Layout for the card

		layout = MDFloatLayout(size = self.trafficCard.size)

		self.trafficCard.add_widget(layout)

		icon = MDIconButton(icon = 'traffic-light',
			pos_hint = {'center_x': 0.5, 'center_y': 0.6})

		layout.add_widget(icon)

		label = MDLabel(text = 'Traffic Mode',
			pos_hint = {'x': 0, 'y': -0.1},
			halign = 'center',
			font_style = 'Body1')

		descLabel = MDLabel(text = 'Wait through traffic light interval.',
			pos_hint = {'x': 0, 'y': -0.18},
			halign = 'center',
			font_style = 'Caption')

		layout.add_widget(label)
		layout.add_widget(descLabel)

# Statistic screens.

class StatisticScreen(ThemableBehavior, MDFloatLayout, MDScreen):

	def __init__(self, **kwargs):

		super(StatisticScreen, self).__init__(**kwargs)

		self.size = Window.size
		self.md_bg_color = self.theme_cls.primary_light

		self.carousel = MDCarousel(direction = 'right',
		loop = True)

		self.timeFrameLayout = MDFloatLayout(size = Window.size)
		self.carousel.add_widget(self.timeFrameLayout)

		self.freeModeLayout = MDFloatLayout(size = Window.size)
		self.carousel.add_widget(self.freeModeLayout)

		self.trafficModeLayout = MDFloatLayout(size = Window.size)
		self.carousel.add_widget(self.trafficModeLayout)
	
		self.add_widget(self.carousel)

		self.makeTimeFrameCard()
		self.makeTrafficCard()
		self.makeFreeModeCard()

	def labelCard(self, parent, size_hint=(0.5, 0.5), pos_hint = {'center_x': .5, 'center_y': .5},
	title='Title of card.', 
	description='Description for card.'):

		card = MDCard(radius = 15,
		md_bg_color = self.theme_cls.accent_light,
		size_hint = size_hint,
		pos_hint = pos_hint,
		elevation = 8,
		ripple_behavior = True)

		parent.add_widget(card)

		layout = MDFloatLayout(size = card.size)
		card.add_widget(layout)

		title = MDLabel(text = title,
		font_style = 'H4',
		halign = 'center',
		valign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6})

		description = MDLabel(text = description,
		font_style = 'Subtitle1',
		halign = 'center',
		valign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .4})

		layout.add_widget(title)
		layout.add_widget(description)

	def makeTimeFrameCard(self):

		card = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		size_hint = (0.85, 0.85),
		pos_hint = center,
		elevation = 8)

		self.timeFrameLayout.add_widget(card)

		layout = MDFloatLayout(size = card.size)
		card.add_widget(layout)

		title = MDLabel(text = 'Time Frame Statistics.',
		font_style = 'H2',
		halign = 'center',
		valign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .875})
		layout.add_widget(title)

		streaks = self.retrieve('streak', 'streak_high_score')

		try:
			self.timeFramePlayed = len(streaks)

			self.highestStreak = max(streaks)

		except:
			self.highestStreak = 0

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .5, "center_y": .65},
		description = 'Highest Streak',
		title = str(self.highestStreak))

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .5, "center_y": .425},
		description = 'Average Reaction Time',
		title = '?')

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .5, "center_y": .2},
		description = 'Fastest Reaction',
		title = '12 ms')

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .775, "center_y": .65},
		description = 'Times Played',
		title = str(self.timeFramePlayed))

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .775, "center_y": .425},
		description = 'Total streaks gained',
		title = '14')

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .775, "center_y": .2},
		description = 'Total time spent waiting',
		title = '?')

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .225, "center_y": .65},
		description = 'Times reacted early',
		title = '?')

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .225, "center_y": .425},
		description = 'Times reacted late',
		title = '?')

		self.labelCard(parent = layout, 
		size_hint = (0.25, 0.2),
		pos_hint = {'center_x': .225, "center_y": .2},
		description = 'Streaks lost',
		title = '19')

	def makeTrafficCard(self):

		card = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		size_hint = (0.85, 0.85),
		pos_hint = center,
		elevation = 8)

		self.trafficModeLayout.add_widget(card)

		layout = MDFloatLayout(size = card.size)
		card.add_widget(layout)

		title = MDLabel(text = 'Traffic Mode Statistics',
		font_style = 'H2',
		halign = 'center',
		valign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .875})

		layout.add_widget(title)
	
	def makeFreeModeCard(self):

		card = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		size_hint = (0.85, 0.85),
		pos_hint = center,
		elevation = 8)

		self.freeModeLayout.add_widget(card)

		layout = MDFloatLayout(size = card.size)
		card.add_widget(layout)

		title = MDLabel(text = 'Free Mode Statistics.',
		font_style = 'H2',
		halign = 'center',
		valign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .875})

		layout.add_widget(title)

	def on_enter(self):

		Clock.schedule_once(self.get_stats)

		Clock.schedule_once(self.update_stats)

		print('screen switched to stats')

	def loadScreen(self, screenType):

		self.manager.current = str(screenType)

	def retrieve(self, game, col):

		# Connect to database

		conn = sqlite3.connect('user_stats.db')
		cur = conn.cursor()

		# Retrieve stats and Filter out any NoneType

		stats = [stat[0] for stat in cur.execute(f"SELECT {col} FROM {game}_stats")]
		stats = list(filter(None, stats))

		# Close connection to databse

		conn.close()

		# Return the smallest value recorded.

		return stats

	def update_stats(self, dt=None):

		pass

	def get_stats(self, dt=None):

		try:

			self.highestStreak = max(self.retrieve('streak', 'streak_high_score'))

		except:

			self.highestStreak = 0
# Reaction Screens.

class ReactionScreen(ThemableBehavior, MDFloatLayout, MDScreen):

	def __init__(self, **kwargs):

		super(ReactionScreen, self).__init__(**kwargs)

		global yellow
		global red
		global green

		self.size = Window.size
		self.resetting = False

		self.reactButton = Button(text = 'Tap to start.', 
			background_normal = '',
			background_color = red, 
			halign = 'center')
		self.reactButton.bind(on_press = self.ready)
		self.add_widget(self.reactButton)

		self.returnButton = MDIconButton(icon = 'arrow-left',
		pos_hint = {'center_x': .075, 'center_y': .925},
		user_font_size = 48,
		md_bg_color_disabled = (0, 0, 0, 0),
		md_bg_color = (0, 0, 0, 0))

		self.returnButton.bind(on_press = lambda event, x='Modes': self.loadScreen(screenType=x))
		self.add_widget(self.returnButton)

	def on_enter(self):
		self.resetting = False

		try:
			self.timer.cancel()

		except:
			print('no timers')

		self.reactButton.background_down = 'atlas://data/images/defaulttheme/button_pressed'
		self.reactButton.text = 'Tap to start.'
		self.reactButton.background_color = red
		self.reactButton.unbind(on_press = self.react)
		self.reactButton.unbind(on_press = self.restart)
		self.reactButton.bind(on_press = self.ready)
	
	def exit(self, event=None):

		self.returnButton.disabled = False
		self.returnButton.md_bg_color = (0, 0, 0, 0)

		self.settings.disabled = False
		self.settings.md_bg_color = (0, 0, 0, 0)


		self.reactButton.disabled = False
		anim = Animation(opacity = 0, duration = 0.5)
		anim.start(self.card)
		anim.bind(on_complete = lambda event, instance: self.remove_widget(instance))

	def reset(self):

		self.reactButton.unbind(on_press = self.restart)

		self.reactButton.text = 'Tap to start.'
		self.reactButton.background_color = red
		self.reactButton.bind(on_press = self.ready)

	def loadScreen(self, screenType):

		self.resetting = True
		self.reactButton.background_down = ''

		try:

			self.timer.cancel()
			self.reactButton.unbind(on_press = self.react)

		except:

			print('Must be that no timers are active.')

		# self.title can be used to load a screen as this will ALWAYS exist when 
		# loading a menu from the ReactionScreen.

		self.manager.current = f'{str(screenType)}'

		try:
			self.exit()

		except:

			print('settings card not open.')

		resetTimer = Timer(0.5, self.reset)
		resetTimer.start()

	def makeExitCard(self, parent):
		
		exitCard = MDCard(radius = (15, 5, 5, 15),
		elevation = 8,
		md_bg_color = self.theme_cls.accent_light,
		size_hint = (0.445, 0.08),
		ripple_behavior = True,
		on_release = self.exit,
		pos_hint = {'center_x': .27, 'center_y': .075})

		parent.add_widget(exitCard)	

		exitLabel = MDLabel(text = 'Exit',
		halign = 'center',
		pos_hint = center)

		exitCard.add_widget(exitLabel)

	def makeMenuCard(self, parent):

		menuCard = MDCard(radius = (5, 15, 15, 5),
		elevation = 8,
		md_bg_color = self.theme_cls.accent_light,
		size_hint = (0.445, 0.08),
		ripple_behavior = True,
		on_release = lambda event, x='Menu': self.loadScreen(screenType=x),
		pos_hint = {'center_x': .73, 'center_y': .075})

		parent.add_widget(menuCard)

		menuLabel = MDLabel(text = 'Main Menu',
		halign = 'center',
		pos_hint = center)

		menuCard.add_widget(menuLabel)

	def ready(self, event=None):

		if self.resetting:
			return

		self.reactButton.unbind(on_press = self.ready)
		self.reactButton.bind(on_press = self.react)

		self.reactButton.text = 'Wait for green.'

		self.wait()

	def restart(self, event=None):

		self.reset()

		# UNBIND button from restart and BIND to react
		self.reactButton.unbind(on_press = self.ready)
		self.reactButton.unbind(on_press = self.restart)
		self.reactButton.bind(on_press = self.react)

		# Reset the button parameters to initial

		self.reactButton.background_color = red
		self.reactButton.text = 'Wait for green'

		self.wait()

	def updateGreen(self, event=None):

		self.reactButton.background_color = green
		self.reactButton.text = 'REACT'

		self.start = time.time()

	def msConvert(self, time, event=None):
		time *= 1000
		time = round(time)
		self.ms = True
		return time

	def earlyReaction(self, event=None):

		try:
			self.cycles = 0
		
		except:
			print('no cycles - not in traffic mode!')

		self.timer.cancel()
		self.reactButton.background_color = yellow
		self.reactButton.text = 'Too Soon!\n\nTap again to restart.'

		self.reactButton.unbind(on_press = self.react)
		self.reactButton.bind(on_press = self.restart)

	def react(self, event = None):

		self.end = time.time()

		if self.timer.is_alive():

			print('timer is alive.')

			self.earlyReaction()
			return

		else:

			reactionTime = self.end - self.start
			reactionTime = self.msConvert(time=reactionTime)

			self.reactButton.text = f'\nYou took {reactionTime} milliseconds to react\n\nAfter waiting {self.waitTime} seconds\n\nTap again to restart.'
		try:
			if self.random:
				self.submit(score = reactionTime)
			else:

				self.submit(score = reactionTime, mode = int2word[self.waitTime])

		except:

			print('self.random doesnt exist u are probably submitting from streak or traffic')


		self.reactButton.unbind(on_press = self.react)
		self.reactButton.bind(on_press = self.restart)

class TimeFrameReaction(ReactionScreen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.title = 'Random'

		self.streak = 0
		self.reactTime = 300

		self.min = 2
		self.max = 5
		self.random = False

		self.streakDisplay()

		self.settings = MDIconButton(icon = 'dots-vertical',
		pos_hint = {'center_x': .925, 'center_y': .925},
		user_font_size = 48,
		md_bg_color_disabled = (0, 0, 0, 0))

		self.settings.bind(on_press = lambda event: self.settingsCard(parent = self))

		self.add_widget(self.settings)

	def on_pre_enter(self):

		self.getStreak()

		self.streakLabel.text = str(self.streak)

	def getStreak(self):

		conn = sqlite3.connect('user_stats.db')

		cur = conn.cursor()

		currentStreak = [val[0] for val in cur.execute('SELECT current_streak FROM streak_stats')]

		try:
			self.streak = currentStreak[-1]

		except:
			self.streak = 0
		conn.close()

	def streakDisplay(self):

		self.streakCard = MDCard(radius = 25,
		pos_hint = {'center_x': .5, 'center_y': .925},
		size_hint = (0.1, 0.04),
		md_bg_color = self.theme_cls.primary_light)

		self.add_widget(self.streakCard)

		streakLayout = MDFloatLayout(size = self.streakCard.size)
		self.streakCard.add_widget(streakLayout)

		streakIcon = MDIcon(icon = 'flash',
		halign = 'center',
		valign = 'center',
		pos_hint = {'center_x': 0.33, 'center_y': .5})

		self.streakLabel = MDLabel(text = str(self.streak),
		font_style = 'Subtitle2',
		valign = 'center',
		halign = 'center',
		pos_hint = {'center_x': .66, 'center_y': .5})

		streakLayout.add_widget(streakIcon)
		streakLayout.add_widget(self.streakLabel)

	def settingsCard(self, parent):

		if self.reactButton.background_color == list(green) or self.reactButton.background_color == list(yellow):

			self.reactButton.disabled = True
			self.reactButton.background_disabled_normal = ''

		else:

			self.reactButton.background_color = red
			self.reactButton.text = 'Tap to start.'
			self.reactButton.unbind(on_press = self.react)
			self.reactButton.unbind(on_press = self.restart)
			self.reactButton.bind(on_press = self.ready)
			self.reactButton.disabled = True
			self.reactButton.background_disabled_normal = ''

		try:
			self.timer.cancel()

		except:

			print('no timers active')

		self.settings.disabled = True
		self.returnButton.disabled = True

		self.card = MDCard(radius = 15,
		pos_hint = center,
		size_hint = (0.5, 0.7),
		md_bg_color = self.theme_cls.primary_light,
		line_color = (0.5, 0.5, 0.5, 1),
		opacity = 0,
		elevation = 12)

		parent.add_widget(self.card)
		fadein = Animation(opacity = 1, duration = 0.2)
		fadein.start(self.card)

		self.cardLayout = MDFloatLayout(size = self.card.size)
		self.card.add_widget(self.cardLayout)

		title = MDLabel(text = 'Settings',
		pos_hint = {'center_x': .5, 'center_y': .9},
		halign = 'center',
		font_style = 'H3')
		self.cardLayout.add_widget(title)

		if self.random:
			self.makeRandomCard(parent = self.cardLayout, 
			pos = {'center_x': .5, 'center_y': .46})

			self.randSwitch.active = True
			
		else:

			self.setTimeCard()
			self.makeRandomCard(parent = self.cardLayout)

		self.reactTimeCard()
		self.makeExitCard(parent = self.cardLayout)
		self.makeMenuCard(parent = self.cardLayout)

	def reactTimeCard(self):

		self.reactCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		pos_hint = {'center_x': .5, 'center_y': 0.7},
		size_hint = (0.9, 0.225),
		elevation = 8)
		self.cardLayout.add_widget(self.reactCard)

		layout = MDFloatLayout(size = self.reactCard.size)
		self.reactCard.add_widget(layout)

		self.reactSlider = MDSlider(min = 50,
		max = 300,
		step = 1,
		size_hint = (0.9, 0.1),
		pos_hint = {'center_x': .5, 'center_y': .3},
		hint_bg_color = self.theme_cls.accent_color,
		hint_text_color = self.theme_cls.accent_color,
		color = self.theme_cls.accent_color,
		hint = True,
		value = 300)
		self.reactSlider.bind(value = self.changeReactTime)

		layout.add_widget(self.reactSlider)

		reactLabel = MDLabel(text = 'Maximum Reaction Time',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')
		
		descLabel = MDLabel(text = 'Choose how quickly you need to react.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')

		layout.add_widget(reactLabel)
		layout.add_widget(descLabel)

	def setTimeCard(self):

		self.setCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		pos_hint = {'center_x': .5, 'center_y': 0.46},
		size_hint = (0.9, 0.225),
		elevation = 8)
		self.cardLayout.add_widget(self.setCard)

		layout = MDFloatLayout(size = self.setCard.size)
		self.setCard.add_widget(layout)

		self.setTimeSlider = MDSlider(min = 2,
		max = 5,
		step = 1,
		size_hint = (0.9, 0.1),
		pos_hint = {'center_x': .5, 'center_y': .3},
		hint_bg_color = self.theme_cls.accent_color,
		hint_text_color = self.theme_cls.accent_color,
		color = self.theme_cls.accent_color,
		hint = True,
		show_off = False)
		self.setTimeSlider.bind(value = self.changeSetTime)

		layout.add_widget(self.setTimeSlider)

		setLabel = MDLabel(text = 'Wait Time',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')
		
		descLabel = MDLabel(text = 'Choose how long to wait for.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')

		layout.add_widget(setLabel)
		layout.add_widget(descLabel)

	def makeRandomCard(self, parent, pos = {'center_x': .5, 'center_y': .23}):
		
		self.randomCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		ripple_behavior = True,
		pos_hint = pos,
		size_hint = (0.9, 0.2),
		elevation = 8)
		parent.add_widget(self.randomCard)

		layout = MDFloatLayout(size = self.randomCard.size)
		self.randomCard.add_widget(layout)

		randomLabel = MDLabel(text = 'Random wait time?',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')

		descLabel = MDLabel(text = 'Generate a random wait time.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')

		self.randSwitch = MDCheckbox(selected_color = self.theme_cls.accent_light,
		unselected_color = self.theme_cls.accent_color,
		_no_ripple_effect = True,
		size_hint = (1, 0.66),
		pos_hint = {'center_x': 0.5, 'center_y': 0.33},
		on_press = self.randSwitchPressed)

		layout.add_widget(self.randSwitch)
		layout.add_widget(randomLabel)
		layout.add_widget(descLabel)

	def changeSetTime(self, event, value):

		print(value)

	def changeReactTime(self, event, value):

		self.reactTime = value

	def randSwitchPressed(self, event=None):

			if self.randSwitch.active == True:

				# The random card will slide to the 'target position' of the slide cards current position.

				targetPos = self.setCard.pos_hint

				# animations
				
				fade = Animation(opacity = 0, duration = 0.2)
				fade.start(self.setCard)
				fade.bind(on_complete = lambda anim, widget: self.cardLayout.remove_widget(self.setCard))

				pos = Animation(pos_hint = targetPos,
				duration = 1.5,
				transition = 'in_out_quint')
				pos.start(self.randomCard)

				# important to know if the random screen needs to be displayed when switching between menus

				self.random = True

			else:

				try:
					self.waitTime = self.setValue

				except:

					print('set value slider not changed yet.')

				self.cardLayout.add_widget(self.setCard)


				# This prevents small bugs from happening if user spams the random card.

				self.setCard.opacity = 0

				fade = Animation(opacity = 1, duration = 1.5, transition = 'in_expo')

				pos = Animation(pos_hint = {'center_x': 0.5, 'center_y': 0.23}, 
				duration = 1.5,
				transition = 'in_out_quint')

				fade.start(self.setCard)
				pos.start(self.randomCard)


				self.random = False

	def wait(self, event=None):

		if self.random:
			self.waitTime = round(uniform(self.min, self.max), 2)

		else:

			try:

				self.waitTime = self.setTimeSlider.value

			except:

				self.waitTime = 2

		print('wait time:', self.waitTime, 'seconds')

		self.timer = Timer(self.waitTime, self.updateGreen)
		self.timer.start()

	def react(self, event=None):

		self.end = time.time()

		if self.timer.is_alive():

			self.earlyReaction()
			self.streak = 0
			blueAnim = Animation(md_bg_color = self.theme_cls.accent_color, d = 0.1)
			whiteAnim = Animation(md_bg_color = self.theme_cls.primary_light, d = 1, t = 'in_cubic')

			blueAnim.start(self.streakCard)
			blueAnim.bind(on_complete = lambda event, instance: whiteAnim.start(self.streakCard))

			fadeOut = Animation(opacity = 0, d = 0.2)
			fadeIn = Animation(opacity = 1, d = 0.2)

			fadeOut.start(self.streakLabel)

			fadeOut.bind(on_complete = self.streakLabelChange)
			fadeOut.bind(on_complete = lambda anim, instance: fadeIn.start(self.streakLabel))
			return

		else:

			reactionTime = self.end - self.start
			reactionTime = self.msConvert(time=reactionTime)

			if reactionTime > self.reactTime:
				
				self.reactButton.background_color = red
				self.reactButton.text = f'You took too long to react.\n\n{reactionTime} ms\n\nBye Bye streak.'

				self.streak = 0
				self.submit(zero=True)

				blueAnim = Animation(md_bg_color = self.theme_cls.accent_color, d = 0.2)
				whiteAnim = Animation(md_bg_color = self.theme_cls.primary_light, d = 1, t = 'in_cubic')

				blueAnim.start(self.streakCard)
				blueAnim.bind(on_complete = lambda event, instance: whiteAnim.start(self.streakCard))


			else:

				self.reactButton.text = f'\nYou took {reactionTime} milliseconds to react\n\nAfter waiting {self.waitTime} seconds\n\nTap again to restart.'
				self.streak += 1
				self.submit()

		fadeOut = Animation(opacity = 0, d = 0.2)
		fadeIn = Animation(opacity = 1, d = 0.2)

		fadeOut.start(self.streakLabel)

		fadeOut.bind(on_complete = self.streakLabelChange)
		fadeOut.bind(on_complete = lambda anim, instance: fadeIn.start(self.streakLabel))


		self.reactButton.unbind(on_press = self.react)
		self.reactButton.bind(on_press = self.restart)

	def streakLabelChange(self, anim, instance):

		self.streakLabel.text = str(self.streak)
	
	def submit(self, zero=False):

		conn = sqlite3.connect('user_stats.db')

		cur = conn.cursor()

		# If streak is reset then we don't need to store it.

		if zero:
			cur.execute(f'''UPDATE streak_stats SET current_streak={self.streak}''')

		else:

			cur.execute(f'''INSERT INTO streak_stats (streak_high_score)
							VALUES ({self.streak})''')
			cur.execute(f'''UPDATE streak_stats SET current_streak={self.streak}''')

		conn.commit()
		conn.close()

class SetReaction(ReactionScreen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.title = 'Set'
		self.waitTime = 1

		self.random = False
		self.vibrate = False

		self.min = 1
		self.max = 5
		self.setValue = 1
		
		self.settings = MDIconButton(icon = 'dots-vertical',
		pos_hint = {'center_x': .925, 'center_y': .925},
		user_font_size = 48,
		md_bg_color_disabled = (0, 0, 0, 0),
		md_bg_color = (0, 0, 0, 0))
		self.settings.bind(on_press = lambda event: self.settingsCard(parent = self))
		self.add_widget(self.settings)

	def settingsCard(self, parent):

		if self.reactButton.background_color == list(green) or self.reactButton.background_color == list(yellow):

			self.reactButton.disabled = True
			self.reactButton.background_disabled_normal = ''

		else:

			self.reactButton.background_color = red
			self.reactButton.text = 'Tap to start.'
			self.reactButton.unbind(on_press = self.react)
			self.reactButton.unbind(on_press = self.restart)
			self.reactButton.bind(on_press = self.ready)
			self.reactButton.disabled = True
			self.reactButton.background_disabled_normal = ''

		try:
			self.timer.cancel()

		except:

			print('no timers active')

		self.settings.disabled = True
		self.returnButton.disabled = True

		self.card = MDCard(radius = 15,
		pos_hint = center,
		size_hint = (0.5, 0.7),
		md_bg_color = self.theme_cls.primary_light,
		line_color = (0.5, 0.5, 0.5, 1),
		opacity = 0,
		elevation = 12)

		parent.add_widget(self.card)
		fadein = Animation(opacity = 1, duration = 0.2)
		fadein.start(self.card)

		self.cardLayout = MDFloatLayout(size = self.card.size)
		self.card.add_widget(self.cardLayout)

		title = MDLabel(text = 'Settings',
		pos_hint = {'center_x': .5, 'center_y': .9},
		halign = 'center',
		font_style = 'H3')
		self.cardLayout.add_widget(title)
		
		if self.random:

			self.makeRandomCard(parent = self.cardLayout, 
			pos = {'center_x': .5, 'center_y': .675})

			self.randSwitch.active = True

			self.randomRangeControl(opacity = 1)
			self.makeVibrateCard(pos = {'center_x': .5, 'center_y': .175}, size = (0.9, 0.09))
			
			if self.vibrate:
				self.vibrateSwitch.active = True

			else:
				self.vibrateSwitch.active = False

		else:

			self.sliderCard(parent = self.cardLayout)
			self.makeRandomCard(parent = self.cardLayout)
			self.makeVibrateCard()

			if self.vibrate:
				self.vibrateSwitch.active = True

			else:
				self.vibrateSwitch.active = False

		self.makeExitCard(parent = self.cardLayout)
		self.makeMenuCard(parent = self.cardLayout)
		
	def sliderCard(self, parent):

		self.slideCard = MDCard(radius = 15, 
		md_bg_color = self.theme_cls.primary_color,
		pos_hint = {'center_x': .5, 'center_y': .675},
		size_hint = (0.9, 0.225),
		elevation = 8)
		parent.add_widget(self.slideCard)

		sliderLayout = MDFloatLayout(size = self.slideCard.size)
		self.slideCard.add_widget(sliderLayout)

		setSlider = MDSlider(value = self.waitTime,
		min = 1.0,
		max = 5.0,
		size_hint = (0.9, 0.1),
		pos_hint = {'center_x': 0.5, 'center_y': 0.25},
		step = 1,
		hint_bg_color = self.theme_cls.primary_light,
		hint_text_color = self.theme_cls.accent_color,
		color = self.theme_cls.accent_color)
		setSlider.bind(value = lambda instance, value: self.changeWaitTime(value = value))
		sliderLayout.add_widget(setSlider)

		sliderLabel = MDLabel(text = 'Wait time',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')
		sliderLayout.add_widget(sliderLabel)

		descLabel = MDLabel(text = 'Choose how long to wait for.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')
		sliderLayout.add_widget(descLabel)

	def makeRandomCard(self, parent, pos = {'center_x': .5, 'center_y': .44}):
		
		self.randomCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		ripple_behavior = True,
		pos_hint = pos,
		size_hint = (0.9, 0.225),
		elevation = 8)
		parent.add_widget(self.randomCard)

		layout = MDFloatLayout(size = self.randomCard.size)
		self.randomCard.add_widget(layout)

		randomLabel = MDLabel(text = 'Random wait time?',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')

		descLabel = MDLabel(text = 'Generate a random wait time.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')

		self.randSwitch = MDCheckbox(selected_color = self.theme_cls.accent_light,
		unselected_color = self.theme_cls.accent_color,
		_no_ripple_effect = True,
		size_hint = (1, 0.66),
		pos_hint = {'center_x': 0.5, 'center_y': 0.33},
		on_press = self.randSwitchPressed)

		layout.add_widget(self.randSwitch)
		layout.add_widget(randomLabel)
		layout.add_widget(descLabel)

	def makeVibrateCard(self, pos = {'center_x': .5, 'center_y': .2225}, size = (0.9, 0.19)):

		self.vibrateCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		ripple_behavior = True,
		pos_hint = pos,
		size_hint = size,
		elevation = 8)
		self.cardLayout.add_widget(self.vibrateCard)

		layout = MDFloatLayout(size = self.vibrateCard.size)
		self.vibrateCard.add_widget(layout)

		self.vibrateSwitch = MDCheckbox(selected_color = self.theme_cls.accent_light,
		unselected_color = self.theme_cls.accent_color,
		_no_ripple_effect = True,
		size_hint = (1, 0.66),
		pos_hint = {'center_x': 0.5, 'center_y': 0.33},
		on_press = self.vibrateSwitchPressed)

		vibrateLabel = MDLabel(text = 'Vibrate',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')

		layout.add_widget(vibrateLabel)
		layout.add_widget(self.vibrateSwitch)

	def randomRangeControl(self, opacity = 0):

		self.minCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		pos_hint = {'center_x': .5, 'center_y': .475},
		size_hint = (0.9, 0.15),
		elevation = 8,
		opacity = opacity)

		self.cardLayout.add_widget(self.minCard)

		minLayout = MDFloatLayout(size = self.minCard.size)
		self.minCard.add_widget(minLayout)

		self.minSlider = MDSlider(min = 1,
		max = 4,
		step = 1,
		pos_hint = {'center_x': .5, 'center_y': .33},
		hint_text_color = self.theme_cls.accent_color,
		size_hint = (0.9, 0.1),
		color = self.theme_cls.accent_light,
		active = True)
		self.minSlider.bind(value = lambda instance, value: self.minSliderMoved(value = value))

		minDesc = MDLabel(text = 'Min',
		font_style = 'Subtitle2',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75})

		minLayout.add_widget(self.minSlider)
		minLayout.add_widget(minDesc)

		self.maxCard = MDCard(radius = 15,
		md_bg_color = self.theme_cls.primary_color,
		pos_hint = {'center_x': .5, 'center_y': .31},
		size_hint = (0.9, 0.15),
		elevation = 8,
		opacity = opacity)

		self.cardLayout.add_widget(self.maxCard)

		maxLayout = MDFloatLayout(size = self.maxCard.size)
		self.maxCard.add_widget(maxLayout)

		self.maxSlider = MDSlider(min = 2,
		max = 5,
		step = 1,
		pos_hint = {'center_x': .5, 'center_y': .33},
		hint_text_color = self.theme_cls.accent_color,
		size_hint = (0.9, 0.1),
		color = self.theme_cls.accent_light,
		value = 5,
		active = True)
		self.maxSlider.bind(value = lambda instance, value: self.maxSliderMoved(value = value))

		maxDesc = MDLabel(text = 'Max',
		font_style = 'Subtitle2',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75})

		maxLayout.add_widget(self.maxSlider)
		maxLayout.add_widget(maxDesc)

	def minSliderMoved(self, value):

		self.maxSlider.min = value + 1

		self.min = value
		self.waitTime = uniform(self.min, self.max)

	def maxSliderMoved(self, value):

		self.minSlider.max = value -1
		self.max = value
		self.waitTime = uniform(self.min, self.max)

	def changeWaitTime(self, value, event=None):

		self.setValue = value

		self.waitTime = int(value)

	def randSwitchPressed(self, event=None):

		if self.randSwitch.active == True:

			# important to know if the random screen needs to be displayed when switching between menus

			self.random = True

			# Add the range controls to the widget.

			self.randomRangeControl()

			# The random card will slide to the 'target position' of the slide cards current position.

			targetPos = self.slideCard.pos_hint

			# Fade out the set time slider card
			
			fade = Animation(opacity = 0, duration = 0.2)
			fade.start(self.slideCard)

			# When the set time slider card fades, remove the widget from the layout.

			fade.bind(on_complete = lambda anim, widget: self.cardLayout.remove_widget(self.slideCard))

			# Slow fade in for the minimum and maximum time cards.

			rangeFade = Animation(opacity = 1, duration = 1.5, transition = 'in_expo')

			# Position animation for the random card

			pos = Animation(pos_hint = targetPos,
			duration = 1.5,
			transition = 'in_out_quint')

			
			pos.start(self.randomCard)
			rangeFade.start(self.minCard)
			rangeFade.start(self.maxCard)

			# Size animation for the vibration card

			size = Animation(size_hint = (0.9, 0.09), d = 1.5, t = 'in_out_quint')
			size.start(self.vibrateCard)

			vibratePos = Animation(pos_hint = {'center_x': .5, 'center_y': .175}, d = 1.5, t = 'in_out_quint')
			vibratePos.start(self.vibrateCard)

		else:

			try:
				self.waitTime = self.setValue

			except:

				print('set value slider not changed yet.')

			# Random settings aren't activated, this must be reflected in the self.random var.

			self.random = False

			self.cardLayout.add_widget(self.slideCard)


			# This prevents small bugs from happening if user spams the random card.

			self.slideCard.opacity = 0

			# Slow fade in for slide card

			fade = Animation(opacity = 1, duration = 1.5, transition = 'in_expo')

			# Reposition animation for random card

			pos = Animation(pos_hint = {'center_x': 0.5, 'center_y': 0.44}, 
			duration = 1.5,
			transition = 'in_out_quint')

			# Size and position animation for vibration card

			vibratePos = Animation(pos_hint = {'center_x': .5, 'center_y': .2225}, d = 1.5, t = 'in_out_quint')

			vibrateSize = Animation(size_hint = (0.9, 0.19), d = 1.5, t = 'in_out_quint')

			# Quick fade out for minimum and maximum card

			rangeFade = Animation(opacity = 0, duration = 0.2)
			rangeFade.start(self.minCard)
			rangeFade.start(self.maxCard)

			# When the minimum and maximum cards fade out, start fading in the slider card
			# AND moving the random card.

			rangeFade.bind(on_complete = lambda anim, card: fade.start(self.slideCard))
			rangeFade.bind(on_complete = lambda anim, card: pos.start(self.randomCard))

			rangeFade.bind(on_complete = lambda anim, card: vibratePos.start(self.vibrateCard))
			rangeFade.bind(on_complete = lambda anim, card: vibrateSize.start(self.vibrateCard))

			# Once the minimum and maximum cards have faded out, remove them from the widget tree.

			rangeFade.bind(on_complete = lambda anim, card: self.cardLayout.remove_widget(self.minCard))
			rangeFade.bind(on_complete = lambda anim, card: self.cardLayout.remove_widget(self.maxCard))

	def vibrateSwitchPressed(self, event=None):

		if self.vibrateSwitch.active == True:

			self.vibrate = True

		else:

			self.vibrate = False

	def removeCard(self, event, card):

		self.remove_widget(card)

	def wait(self, event=None):

		if self.random:
			self.waitTime = round(uniform(self.min, self.max), 2)

		print('wait time:', self.waitTime, 'seconds')

		self.timer = Timer(self.waitTime, self.updateGreen)
		self.timer.start()

	def submit(self, score, mode=None, event=None):

		conn = sqlite3.connect('user_stats.db')

		cur = conn.cursor()

		if self.random:

			print(f'random score: ', {score})
			cur.execute(f'''INSERT INTO random_stats (high_score)
							VALUES ({score})''')

		else:

			print(f'{mode}_second score: {score}')

			cur.execute(f'''INSERT INTO set_stats ({mode}_second) 
							VALUES ({score})''')

		conn.commit()
		conn.close()

class TrafficReaction(ReactionScreen):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.title = 'Traffic'

		self.purple = (0.349, 0, 0.49, 1)
		self.blue = (0.027, 0, 0.682, 1)
		self.orange = (0.874, 0.552, 0, 1)
		self.pink = (0.937, 0.047, 0.956, 1)

		self.cycles = 0

		self.colours = {0: yellow, 
		1: self.purple, 
		2: self.blue, 
		3: self.orange, 
		4: self.pink}

		self.waitInterval = 1
		self.numberOfColours = 1

		self.settings = MDIconButton(icon = 'dots-vertical',
		pos_hint = {'center_x': .925, 'center_y': .925},
		user_font_size = 48,
		md_bg_color_disabled = (0, 0, 0, 0),
		md_bg_color = (0, 0, 0, 0))
		self.settings.bind(on_press = lambda event: self.settingsCard(parent = self))
		self.add_widget(self.settings)

	def settingsCard(self, parent):

		if self.reactButton.background_color == list(green) or self.reactButton.background_color == list(yellow):

			self.reactButton.disabled = True
			self.reactButton.background_disabled_normal = ''

		else:

			self.reactButton.background_color = red
			self.reactButton.text = 'Tap to start.'
			self.reactButton.unbind(on_press = self.react)
			self.reactButton.unbind(on_press = self.restart)
			self.reactButton.bind(on_press = self.ready)
			self.reactButton.disabled = True
			self.reactButton.background_disabled_normal = ''

		try:
			self.timer.cancel()

		except:

			print('no timers active')

		self.settings.disabled = True
		self.returnButton.disabled = True

		self.card = MDCard(radius = 15,
		pos_hint = center,
		size_hint = (0.5, 0.7),
		md_bg_color = self.theme_cls.primary_light,
		line_color = (0.5, 0.5, 0.5, 1),
		opacity = 0,
		elevation = 12)

		parent.add_widget(self.card)
		fadein = Animation(opacity = 1, duration = 0.2)
		fadein.start(self.card)

		self.cardLayout = MDFloatLayout(size = self.card.size)
		self.card.add_widget(self.cardLayout)

		title = MDLabel(text = 'Settings',
		pos_hint = {'center_x': .5, 'center_y': .9},
		halign = 'center',
		font_style = 'H3')
		self.cardLayout.add_widget(title)

		self.makeIntervalCard()
		self.makeNumberColourCard()

		self.makeExitCard(parent = self.cardLayout)
		self.makeMenuCard(parent = self.cardLayout)

	def makeIntervalCard(self):

		intervalCard = MDCard(radius = 15,
		pos_hint = {'center_x': .5, 'center_y': .64},
		size_hint = (0.9, 0.32),
		md_bg_color = self.theme_cls.primary_color)
		self.cardLayout.add_widget(intervalCard)

		layout = MDFloatLayout(size = intervalCard.size)
		intervalCard.add_widget(layout)

		self.intervalSlider = MDSlider(min = 1,
		max = 5,
		step = 1,
		hint = True,
		hint_text_color = self.theme_cls.accent_color,
		color = self.theme_cls.accent_color,
		size_hint = (0.9, 0.1),
		pos_hint = {'center_x': .5, 'center_y': .33},
		value = self.waitInterval)
		self.intervalSlider.bind(value = lambda event, value: self.changeWaitTime(value = value))
		layout.add_widget(self.intervalSlider)

		intervalLabel = MDLabel(text = 'Interval Time',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')

		descLabel = MDLabel(text = 'Wait time between each colour change.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')

		layout.add_widget(intervalLabel)
		layout.add_widget(descLabel)

	def makeNumberColourCard(self):

		self.numberColourCard = MDCard(radius = 15,
		pos_hint = {'center_x': .5, 'center_y': .3},
		size_hint = (0.9, 0.32),
		md_bg_color = self.theme_cls.primary_color)
		self.cardLayout.add_widget(self.numberColourCard)

		layout = MDFloatLayout(size = self.numberColourCard.size)
		self.numberColourCard.add_widget(layout)

		self.colourSlider = MDSlider(min = 1,
		max = 5,
		step = 1,
		hint = True,
		hint_text_color = self.theme_cls.accent_color,
		color = self.theme_cls.accent_color,
		size_hint = (0.9, 0.1),
		pos_hint = {'center_x': .5, 'center_y': .33},
		value = self.numberOfColours)
		self.colourSlider.bind(value = lambda event, value: self.changeNumberOfColours(value = value))
		layout.add_widget(self.colourSlider)

		colourLabel = MDLabel(text = 'Number of colours',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .75},
		font_style = 'H6')

		descLabel = MDLabel(text = 'How many colours before green.',
		halign = 'center',
		pos_hint = {'center_x': .5, 'center_y': .6},
		font_style = 'Subtitle2')

		layout.add_widget(colourLabel)
		layout.add_widget(descLabel)

	def changeWaitTime(self, value):

		print(value)

		self.waitInterval = value

	def changeNumberOfColours(self, value):

		print(value)

		self.numberOfColours = value

	def updateColour(self, event=None):

		self.cycles += 1

		self.reactButton.background_color = choice(self.colours)

		if self.cycles == self.numberOfColours:
			self.waitGreen()

		else:
			self.wait()

	def waitGreen(self, event=None):

		self.cycles = 0

		self.timer = Timer(self.waitInterval, self.updateGreen)
		self.timer.start()

	def wait(self, event=None):

		self.waitTime = self.waitInterval + (self.numberOfColours * self.waitInterval)


		self.timer = Timer(self.waitInterval, self.updateColour)
		self.timer.start()	

	def submit(self, score, mode=None, event=None):

		conn = sqlite3.connect('user_stats.db')

		cur = conn.cursor()

		cur.execute(f'INSERT INTO traffic_stats VALUES (:high_score)',
			{
				 'high_score': score
			})

		conn.commit()
		conn.close()

# Main build

class React(MDApp):

	def build(self):

		Window.bind(on_keyboard = self.key_input)

	# Theming

		self.theme_cls.primary_palette = "Yellow"
		self.theme_cls.primary_hue = "100"
		self.theme_cls.primary_light_hue = '50'


		self.theme_cls.accent_palette = "Blue"
		self.theme_cls.accent_hue = "200"
		self.theme_cls.accent_light_hue = '100'

	# SQLite3 create database

		conn = sqlite3.connect('user_stats.db')

		cur = conn.cursor()
		cur.execute('''CREATE TABLE if not exists set_stats(
			one_second INTEGER,
			two_second INTEGER,
			three_second INTEGER,
			four_second INTEGER,
			five_second INTEGER,
			random REAL)
		 ''')

		cur.execute('''CREATE TABLE if not exists traffic_stats(
			high_score INTEGER,
			wait_time INTEGER)
			''')

		cur.execute('''CREATE TABLE if not exists streak_stats(
			streak_high_score INTEGER,
			current_streak INTEGER,
			wait_time INTEGER)
			''')

		conn.commit()
		conn.close()

	# Screen Manager

		self.sm = ScreenManager(transition = FadeTransition(duration=0.2))

		# Main menu

		self.sm.add_widget(MainMenu(name = 'Menu'))


		# Game modes menu screen

		self.sm.add_widget(ModeScreen(name = 'Modes'))

		# Reaction screens

		self.sm.add_widget(TimeFrameReaction(name = 'Time Frame'))

		self.sm.add_widget(SetReaction(name = 'Set'))

		self.sm.add_widget(TrafficReaction(name = 'Traffic'))

		# Statistic Screen

		self.sm.add_widget(StatisticScreen(name = 'Statistics'))

		return self.sm

	def key_input(self, window, key, *args):

		if key == 27:

			self.sm.current = 'Menu'

			return True

		elif key == 97:

			self.sm.current = 'Menu'

			return True

		else:
			return False

# Run the build.

if __name__ == '__main__':

	React().run()



