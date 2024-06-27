import pygame
from time import strftime

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước cửa sổ nhỏ hơn
screen_width = 200  # Giảm kích thước chiều rộng
screen_height = 100  # Giảm kích thước chiều cao
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("A digital clock")

# Định nghĩa màu sắc
GREY = (120, 120, 120)
WHITE = (255, 255, 255)

# Tạo đối tượng font
font = pygame.font.Font(None, 40)

# Hàm để render thời gian
def render_time():
    current_time = strftime('%H:%M:%S %p')
    text_surface = font.render(current_time, True, WHITE)
    return text_surface

# Đặt "is_running" thành True ban đầu
is_running = True

# Bắt đầu chạy chương trình
while is_running:
    screen.fill(GREY)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Render thời gian hiện tại và blit nó lên màn hình
    time_surface = render_time()
    # Điều chỉnh vị trí của số để phù hợp với kích thước cửa sổ mới
    screen.blit(time_surface, (20, 30))  # Điều chỉnh vị trí theo nhu cầu

    # Cập nhật hiển thị
    pygame.display.flip()

# Thoát pygame
pygame.quit()