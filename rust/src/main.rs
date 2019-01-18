extern crate sdl2;
extern crate gl;

fn main() {
    let sdl = sdl2::init().unwrap();
    let video_sdl = sdl.video().unwrap();
    let window = video_sdl.window("demo", 320, 240).opengl().build().unwrap();
    let _context = window.gl_create_context().unwrap();

    // register a way to load function pointers
    let _gl = gl::load_with(
        |s| video_sdl.gl_get_proc_address(s) as *const std::os::raw::c_void    
    );
    
    let mut event_pump = sdl.event_pump().unwrap();
    'main:loop {
        for event in event_pump.poll_iter() {
            match event {
                sdl2::event::Event::Quit {..} => break 'main,
                _ => {},
            }
        }
        unsafe{
            gl::ClearColor(0.1, 0.2, 0.3, 1.0);
            gl::Clear(gl::COLOR_BUFFER_BIT);
        }
        window.gl_swap_window();
    }

}

