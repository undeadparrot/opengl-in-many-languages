module Lib
    ( someFunc
    ) where

import qualified Graphics.Rendering.OpenGL as GL
import qualified Graphics.UI.GLFW as GLFW

someFunc :: IO ()
someFunc = do
  GLFW.init
  GLFW.windowHint (GLFW.WindowHint'ContextVersionMajor 3)
  GLFW.windowHint (GLFW.WindowHint'ContextVersionMinor 2)
  GLFW.windowHint (GLFW.WindowHint'OpenGLForwardCompat True)
  GLFW.windowHint (GLFW.WindowHint'OpenGLProfile GLFW.OpenGLProfile'Core)
  mwin <- GLFW.createWindow 320 240 "Demo" Nothing Nothing
  case mwin of
    Nothing -> putStrLn "createWindow failed"
    Just win -> do
      GLFW.makeContextCurrent( Just win )
      display win

display win = do
  GL.clearColor GL.$= GL.Color4 0.1 0.2 0.3 1.0
  GL.clear [ GL.ColorBuffer ]
  GLFW.swapBuffers win
  GLFW.pollEvents
  display win 


