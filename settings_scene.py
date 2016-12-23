# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import sound
from credits_scene import *

class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/settings.JPG', 
                                 parent = self, 
                                 size = self.size,
                                 position = self.size/2)
                                 
        back_button_position = Vector2(self.size_of_screen_x * 0.1, self.size_of_screen_y * 0.87)
        self.back_button = SpriteNode('assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 1.5)
                                       
        credits_button_position = Vector2(self.size_of_screen_x/2.5, self.size_of_screen_y/6)
        self.credits_button = SpriteNode('assets/sprites/instructions_button.PNG',
                                              parent = self,
                                              position = credits_button_position,
                                              scale = 0.2)
                                              
        credits_label_postion = Vector2(self.size_of_screen_x/1.8, self.size_of_screen_y/6)
        self.credits_label = LabelNode(text = 'Credits',
                                     font = ('Helvetica', 50),
                                     parent = self,
                                     color = 'black',
                                     position = credits_label_postion)
                                              
        volume_on_button_position = Vector2(self.size_of_screen_x/2.5, self.size_of_screen_y/2)
        self.volume_on_button = SpriteNode('assets/sprites/sound_on.PNG',
                                           parent = self,
                                           position = volume_on_button_position,
                                           scale = 2)
                                           
        volume_off_button_position = Vector2(self.size_of_screen_x/1.65, self.size_of_screen_y/2)
        self.volume_off_button = SpriteNode('assets/sprites/sound_off.PNG',
                                           parent = self,
                                           position = volume_off_button_position,
                                           scale = 2)
        sound_on_label_postion = Vector2(self.size_of_screen_x/2.5, self.size_of_screen_y/2.7)
        self.sound_on_label = LabelNode(text = 'Sound ON',
                                     font = ('Helvetica', 30),
                                     parent = self,
                                     color = 'black',
                                     position = sound_on_label_postion)
                                     
        sound_off_label_postion = Vector2(self.size_of_screen_x/1.65, self.size_of_screen_y/2.7)
        self.sound_off_label = LabelNode(text = 'Sound OFF',
                                     font = ('Helvetica', 30),
                                     parent = self,
                                     color = 'black',
                                     position = sound_off_label_postion)
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 1.4
            
        if self.credits_button.frame.contains_point(touch.location):
            self.credits_button.scale = 0.15
            
        if self.volume_on_button.frame.contains_point(touch.location):
            self.volume_on_button.scale = 1.5
        
        if self.volume_off_button.frame.contains_point(touch.location):
            self.volume_off_button.scale = 1.5
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = 1.5
            sound.play_effect('./assets/Sounds/Drums_02.caf')
            self.dismiss_modal_scene()
            
        if self.credits_button.frame.contains_point(touch.location):
            self.credits_button.scale = 0.2
            sound.play_effect('./assets/Sounds/Drums_02.caf')
            self.present_modal_scene(CreditsScene())
            
        if self.volume_on_button.frame.contains_point(touch.location):
            self.volume_on_button.scale = 2
            #sound.play_effect('drums:Drums_02')
            sound.set_volume(1)
            sound.play_effect('./assets/Sounds/Drums_02.caf')
            
        if self.volume_off_button.frame.contains_point(touch.location):
            self.volume_off_button.scale = 2
            sound.set_volume(0)
    
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
    
