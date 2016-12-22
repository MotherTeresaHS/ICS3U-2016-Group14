# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from game_scene import *
from settings_scene import *
from instructions_scene import *
import time

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/main_menu.JPG', 
                                     parent = self, 
                                     size = self.size,
                                     position = self.size/2)
                                     
        play_button_position = self.size/2
        play_button_position.y = play_button_position.y - 100
        self.play_button = SpriteNode('./assets/sprites/play_button.JPG',
                                       parent = self,
                                       position = play_button_position,
                                       scale = 0.6)
                                       
        settings_button_position = self.size/2
        settings_button_position.x = settings_button_position.x - 300
        settings_button_position.y = settings_button_position.y - 250
        self.settings_button = SpriteNode('assets/sprites/settings_button.PNG',
                                       parent = self,
                                       position = settings_button_position,
                                       scale = 1.7)
                                       
        instructions_button_position = self.size/2
        instructions_button_position.x = instructions_button_position.x + 300
        instructions_button_position.y = instructions_button_position.y - 250
        self.instructions_button = SpriteNode('assets/sprites/instructions_button.PNG',
                                              parent = self,
                                              position = instructions_button_position,
                                              scale = 0.2)
                                       
                                       
        time.sleep(0.1)
        #self.score_label = LabelNode(text = 'High Score: 0',
                                     #font = ('Helvetica', 20),
                                     #parent = self,
                                     #position = self.size/2)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.play_button.frame.contains_point(touch.location):
            self.play_button.scale = 0.55
            
        if self.settings_button.frame.contains_point(touch.location):
            self.settings_button.scale = 1.6
            
        if self.instructions_button.frame.contains_point(touch.location):
            self.instructions_button.scale = 0.15
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.play_button.frame.contains_point(touch.location):
            self.play_button.scale = 0.6
            self.present_modal_scene(GameScene())
            
        if self.settings_button.frame.contains_point(touch.location):
            self.settings_button.scale = 1.7
            self.present_modal_scene(SettingsScene())
            
        if self.instructions_button.frame.contains_point(touch.location):
            self.instructions_button.scale = 0.2
            self.present_modal_scene(InstructionsScene())
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
