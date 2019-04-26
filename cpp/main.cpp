#include "g2d/canvas.hpp"

void keydown(string key) {
    auto pos = mouse_position();
    if (pos.x < 25 && pos.y < 25 and confirm("Exit?")) {
        close_canvas();
    } else {
        set_color({randint(0, 255), randint(0, 255), randint(0, 255)});
        fill_circle({pos.x, pos.y}, 25);
    }
}

int main() {
    init_canvas({640, 480});
    handle_events(nullptr, keydown, nullptr);
    main_loop();
}
