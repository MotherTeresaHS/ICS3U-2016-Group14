# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
from main_menu_scene import *


class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/instructions.JPG', 
                                 parent = self, 
                                 size = self.size,
                                 position = self.size/2)
                                 
        back_button_position = self.size/2
        back_button_position.x = back_button_position.x - 420
        back_button_position.y = back_button_position.y + 285
        self.back_button = SpriteNode('assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 1.5)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 1.4
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 1.5
            self.dismiss_modal_scene()
    
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
    
