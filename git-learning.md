# git-learning

- Khởi tạo repo:
  + git init
  + git init -b <tên nhánh chính>

- Nhánh:
  + Tạo nhánh: git branch <tên nhánh>
  + Xóa nhánh: git branch -d <tên nhánh>
  + Đổi tên nhánh: git branch -m <tên nhánh cũ> <tên nhánh mới>
  + Chuyển nhánh: git switch <tên nhánh>
  + Xem danh sách nhánh: git branch [--a] (xem tất cả nhánh trên remote)
  + Mở giao diện đồ họa trực quan để xem cấu trúc nhánh: gitk --all

- Tương tác với Github (remote):
  + Kết nối với Github bằng SSH key:
    * Bước 1: Kiểm tra đã có SSH key chưa:
      * Linux: ls ~/.ssh
      * Windows: dir C:\Users\TênUser\.ssh
    * Bước 2: Tạo SSH key mới nếu chưa có: ssh-keygen -t ed25519 -C "your_email@example.com"
    * Bước 3: Thêm SSH key public vào Github:
      * Copy nội dung trong file ~/.ssh/id_ed25519.pub
      * GitHub → Settings → SSH and GPG keys → New SSH key
      * Dán nội dung vào và lưu
    * Bước 4: Kiểm tra kết nối: ssh -T git@github.com

  + Tải repo về máy: git clone <remote> [nơi lưu]
    * <remote> có thể là:
      * Đơn giản nhất: URL-repo
      * Nếu có SSH key: git clone git@github.com:<username>/<repository>.git

  + Upload nhánh lên Github: git push -u <remote> <branch>
  + Đồng bộ repo với Github (vẫn giữ local và có thể bị xung đột): git pull <remote> <branch>
    * Cần đồng bộ trước khi push để tránh xung đột
  + Đồng bộ repo với Github (ép local giống Github):
    * git fetch origin (GitHub → cập nhật thông tin Git, chưa sửa file local)
    * git reset --hard origin/main (ép)

- Tương tác với repo:
  + Thêm repo vào cửa sổ hiện tại của vscode: code -a <tên thư mục>
    * Nếu đang đứng ở thư mục muốn repo, <tên thư mục> là dấu "."

- Merge:
  + Đứng ở nhánh đích
  + Hợp nhất nhánh khác vào nhánh hiện tại:
    git merge <tên nhánh khác>

- Commit:
  + Đưa thay đổi vào staging area:
    git add <tên file>
  
  + Xóa file và đưa thay đổi vào staging area:
    git rm <tên file>

  + Tạo commit:
    git commit -m "Thông điệp"

  + Xem commit theo dạng cây: git log --oneline --graph --decorate --all
    --oneline: hiển thị commit ngắn gọn.
    --graph: vẽ sơ đồ ASCII dạng cây để thấy nhánh rẽ.
    --decorate: hiển thị tên nhánh/tag gắn với commit.
    --all: hiển thị tất cả nhánh, không chỉ nhánh hiện tại.
    
  + Hiển thị commit của nhiều nhánh để so sánh: git show-branch

- Khôi phục file về commit trước:
  + git checkout HEAD~1 <tên file>

- Xem cấu hình:
  + Repo hiện tại:
    git config --list

  + Toàn cục:
    git config --global --list

  + Hệ thống:
    git config --system --list

- Cấu hình:
  + git config [--global/--system] <thuộc tính> "..."

  + Ví dụ:
    git config user.name "Nguyen Van A"
    git config user.email "nguyenvana@gmail.com"

- Gỡ Git khỏi thư mục:
  + Bash:
    rm -rf .git

  + PowerShell:
    Remove-Item -Recurse -Force .git
