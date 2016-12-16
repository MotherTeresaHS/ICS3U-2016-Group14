# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import time

from main_menu_scene import *

class LoadingScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/loading.JPG', 
                                 parent = self, 
                                 size = self.size,
                                 position = self.size/2)
                                    
        self.animation_finished = False

    def update(self):
        # this method is called, hopefully, 60 times a second
        if self.animation_finished == False:
            self.loadAnimation()
            
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
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
    
    @ui.in_background
    def loadAnimation(self):
        self.animation_finished = True
        self.background.remove_from_parent()
        self.background = SpriteNode('./assets/sprites/loading_one.JPG', 
                                     parent = self, 
                                     size = self.size,
                                     position = self.size/2)
        #print 'cool1'
            
        
        time.sleep(1)
        self.background.remove_from_parent()
        self.background = SpriteNode('./assets/sprites/loading_two.JPG', 
                                     parent = self, 
                                     size = self.size,
                                     position = self.size/2)
        #print 'cool2'
            
        time.sleep(1)
        self.background.remove_from_parent()
        self.background = SpriteNode('./assets/sprites/loading_three.JPG', 
                                     parent = self, 
                                     size = self.size,
                                     position = self.size/2)
        #print 'cool3'
            
        time.sleep(1)
        self.background.remove_from_parent()
        self.background = SpriteNode('./assets/sprites/loading_four.JPG', 
                                     parent = self, 
                                     size = self.size,
                                     position = self.size/2)
        #print 'cool4'
        time.sleep(1)
        #self.animation_finished = True
        self.present_modal_scene(MainMenuScene())
