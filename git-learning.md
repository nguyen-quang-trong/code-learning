# git-learning

- Khởi tạo repo: `git init`/`git init -b <tên nhánh chính>`

- Nhánh:
  + Tạo nhánh: 
    * Tạo từ commit hiện tại: `git switch -c <ten-nhanh-moi>`
    * Tạo từ nhánh hiện tại (nhân bản): `git branch -c <ten-nhanh-nguon> <ten-nhanh-moi>`

  + Xóa nhánh: `git branch -d <ten-nhanh>`
  + Đổi tên nhánh hiện tại: `git branch -m <ten-nhanh-moi>`
  + Chuyển nhánh: `git switch <ten-nhanh>`
  + Xem danh sách nhánh: `git branch [-a]` (dùng `-a` khi muốn xem cả nhánh của remote)
  + Mở giao diện đồ họa trực quan để xem cấu trúc nhánh: `gitk --all`

- Tương tác với Github (remote):
  + Kết nối với Github bằng SSH key:
    * Bước 1: Kiểm tra đã có SSH key chưa:
      * Linux: `ls ~/.ssh`
      * Windows: `dir C:\Users\TênUser\.ssh`
    * Bước 2: Tạo SSH key mới nếu chưa có: `ssh-keygen -t ed25519 -C "your_email@example.com"`
    * Bước 3: Thêm SSH key public vào Github:
      * Copy nội dung trong file `~/.ssh/id_ed25519.pub`
      * GitHub → Settings → SSH and GPG keys → New SSH key
      * Dán nội dung vào và lưu
    * Bước 4: Kiểm tra kết nối: `ssh -T git@github.com`

  + Tải repo về máy: `git clone <remote> [noi-luu]`
    * `<remote>` có thể là:
      * Đơn giản nhất: URL-repo
      * Nếu có SSH key: `git clone git@github.com:<username>/<repository>.git`

  + Upload nhánh lên Github: `git push -u <remote> <branch>`

- Đồng bộ repo local với repo github:
  + Giữ thay đổi local, đồng bộ github về: `git pull <remote> <branch>`
    * Cần đồng bộ trước khi push để tránh xung đột

  + Bỏ các thay đổi của repo local, ép local giống Github:
    * Bước 1: `git fetch origin` (tải dữ liệu xuống, chưa sửa file local)
    * Bước 2: `git reset --hard origin/main` (ghi đè)

- Merge:
  + Bước 1: Đứng ở nhánh đích
  + Bước 2: Hợp nhất nhánh khác vào nhánh hiện tại:
    * Cách 1: merge bình thường (Giữ lịch sử commit của nhánh được merge): `git merge <ten-nhanh-khac>`
    * Cách 2: squash merge(Gộp các thay đổi thành một commit mới trên nhánh hiện tại.)
      * Bước 2.1: `git merge --squash <ten-nhanh-khac>`
      * Bước 2.2: `git commit -m "thông điệp"`

- Commit:
  + Đưa thay đổi vào stage area: `git add <ten-file>`
  + Xóa file và đưa thay đổi vào staging area: `git rm <ten-file>`
  + Tạo commit:`git commit -m "Thông điệp"`
  + Xem commit theo dạng cây: `git log --oneline --graph --decorate --all`
    `--oneline`: hiển thị commit ngắn gọn.
    `--graph`: vẽ sơ đồ ASCII dạng cây để thấy nhánh rẽ.
    `--decorate`: hiển thị tên nhánh/tag gắn với commit.
    `--all`: hiển thị tất cả nhánh, không chỉ nhánh hiện tại.
  + Hiển thị commit của nhiều nhánh để so sánh: `git show-branch`

- Khôi phục file về trạng thái commit:
  + `git restore <ten-file>`
  + `git restore --source=<commit-hash> <ten-file>`: lấy nội dung của `<ten-file>` từ một commit cũ rồi chép đè lên file hiện tại.
  + Nếu file đã được git add:
    + `git restore --staged <ten-file>`: gỡ file khỏi stage area
    + `git restore <ten-file>`

- Xem cấu hình: `git config [--global/--system] --list`
  + `git config --list`: hiển thị tất cả cấu hình đang có hiệu lực theo thứ tự ưu tiên, gồm system + global + local repo hiện tại.
  + `git config --global --list`: cấu hình của user hiện tại, áp dụng cho tất cả repo của user đó. Thường nằm trong ~/.gitconfig
  + `git config --system --list`: cấu hình toàn hệ thống, áp dụng cho mọi user trên máy. Thường nằm trong file hệ thống của Git.

- Cấu hình:
  + `git config [--global/--system] <thuộc tính> "..."`
  + Ví dụ:
    `git config user.name "Nguyen Van A"`
    `git config user.email "nguyenvana@gmail.com"`

- Gỡ Git khỏi thư mục:
  + Bash: `rm -rf .git`
  + PowerShell: `Remove-Item -Recurse -Force .git`
