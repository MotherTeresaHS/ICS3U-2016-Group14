# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import time

pillar_x = 100
pillar_y = 400

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/game.PNG', 
                                 parent = self, 
                                 size = self.size,
                                 position = self.size/2)
                                 
        self.character_position = Vector2(self.size_of_screen_x * 0.2, self.size_of_screen_y * 0.5)
        self.character = SpriteNode('assets/sprites/alien.png',
                                    parent = self,
                                    position = self.character_position)
                                    #scale = 0.1)
                                    
        
        button_position = Vector2(self.size_of_screen_x * 0.1, self.size_of_screen_y * 0.1)
        self.play_button = SpriteNode('assets/sprites/instructions_button.PNG',
                                 parent = self,
                                 position = button_position,
                                 scale = 12,
                                 alpha = 0.0)
                                 
        self.menu_button = SpriteNode('assets/sprites/menu.png',
                                          parent = self,
                                          position = self.size/2,
                                          scale = 0.5,
                                          alpha = 0.0)
                                          
        bottom_pillar_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y - 60)
        self.pillar_bottom = SpriteNode('assets/sprites/IMG_6446.PNG',
                                        parent = self,
                                        position = bottom_pillar_position,
                                        scale = 0.75,
                                        size = (self.size_of_screen_x*0.2, self.size_of_screen_y*0.75))
                                        
        top_pillar_position = Vector2(self.size_of_screen_x * 0.5, 60)
        self.pillar_top = SpriteNode('assets/sprites/IMG_6446.PNG',
                                        parent = self,
                                        position = top_pillar_position,
                                        scale = 0.75,
                                        size = (self.size_of_screen_x*0.2, self.size_of_screen_y*0.75))
                                        
                                        
        left_side_border_postion = Vector2(self.size_of_screen_x, self.size_of_screen_y)
        self.left_side_border = SpriteNode('assets/sprites/side_borders.PNG',
                                           parent = self,
                                           position = left_side_border_postion,
                                           size = (self.size_of_screen_x/10, self.size_of_screen_y*2))
                                           
        right_side_border_postion = Vector2(0, self.size_of_screen_y)
        self.right_side_border = SpriteNode('assets/sprites/side_borders.PNG',
                                           parent = self,
                                           position = right_side_border_postion,
                                           size = (self.size_of_screen_x/10, self.size_of_screen_y*2))
                                           
        bottom_border_postion = Vector2(self.size_of_screen_x * 0.5, 0)
        self.bottom_border = SpriteNode('assets/sprites/top_and_bottom.PNG',
                                        parent = self,
                                        position = bottom_border_postion,
                                        size = (self.size_of_screen_x*2, self.size_of_screen_y/10))
                                      
        top_border_postion = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y)
        self.top_border = SpriteNode('assets/sprites/top_and_bottom.PNG',
                                        parent = self,
                                        position = top_border_postion,
                                        size = (self.size_of_screen_x*2, self.size_of_screen_y/10))
        #self.fly_bottom = False
        self.current_y_position = self.size_of_screen_y * 0.5
        self.left_or_right = (self.size_of_screen_x * 0.07)*1
        self.left_or_right_left = (self.size_of_screen_x * 0.3)*1
        self.dead = False
        self.menu_button_created = False
        self.score = 0
        self.left_score = False
        self.right_score = False
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        if self.character.frame.intersects(self.left_side_border.frame):
            self.left_or_right = (self.size_of_screen_x * 0.07)* -1
            self.left_or_right_left = (self.size_of_screen_x * 0.3)* -1
            
        if self.character.frame.intersects(self.right_side_border.frame):
            self.left_or_right = (self.size_of_screen_x * 0.07)* 1
            self.left_or_right_left = (self.size_of_screen_x * 0.3)* 1
            
        if self.character.frame.intersects(self.bottom_border.frame) or self.character.frame.intersects(self.top_border.frame):
            #print 'you dead'
            self.dead = True
            
        if self.pillar_top.frame.intersects(self.character.frame) or self.pillar_bottom.frame.intersects(self.character.frame):
            self.dead = True
            
        if self.dead == True:
            self.menu_button.alpha = 1
            self.character.remove_from_parent()
            self.menu_button_created = True

    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        if self.play_button.frame.contains_point(touch.location):
            self.character.run_action(Action.sequence(Action.move_by(self.left_or_right,100,1.5),
                                      Action.move_by(self.left_or_right_left,-2000,13)))
                                      
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = 0.48
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.menu_button.frame.contains_point(touch.location):
            self.menu_button.scale = 0.5
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
        
