// Learn more about F# at http://fsharp.org

open System
open OpenTK
open OpenTK.Graphics 
open OpenTK.Graphics.OpenGL4

type Window(width, height) = 
    inherit GameWindow(
        width, height, Graphics.GraphicsMode.Default, "Demo", GameWindowFlags.Default,
        DisplayDevice.Default, // which display?
        3, 2, GraphicsContextFlags.ForwardCompatible // OpenGL 3.2 context
    )

    override this.OnLoad(e) =
        GL.ClearColor(0.1f, 0.2f, 0.3f, 1.0f)
        base.OnLoad(e)

    override this.OnResize(e) =
        GL.Viewport(0, 0, this.Width, this.Height)
        base.OnResize(e)

    override this.OnRenderFrame(e) =
        GL.Clear ClearBufferMask.ColorBufferBit
        this.Context.SwapBuffers()
        base.OnRenderFrame(e)


[<EntryPoint>]
let main argv =
    printfn "Hello World from F#!"
    use window = new Window(320, 240)
    window.Run()
    0 // return an integer exit code

