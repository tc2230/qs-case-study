
# Flask API 功能實做(搭配 Google cloud logging)

## 概述

Flask API server 實做，搭配 Google Cloud Logging 做記錄功能。

## 環境準備

1. **Docker 和 Docker Compose:** 確認系統裡有安裝 Docker 和 Docker Compose。如果沒有，推薦直接安裝 Docker Desktop：
    - macOS： [Docker Desktop on Mac 官方安裝檔下載](https://docs.docker.com/desktop/install/mac-install/)
    - Windows： [Docker Desktop on Windows 官方安裝檔下載](https://docs.docker.com/desktop/install/windows-install/)

2. **安裝完成後，啟動 Docker Desktop，可於介面左下角確認 Docker Engine 正常執行。如下圖：**
    ![image](https://github.com/user-attachments/assets/67ea61fc-8d75-43c9-bab7-3a6ccb0ea3ea)

3. **可用的 port**: 確保系統上 port **9543** 處於可用狀態。也可以自行修改 `docker-compose.yml` 和 `main.py` 中的port number，兩者一致即可。

## 部署

1. **clone這個專案**
   ```bash
   git clone git@github.com:tc2230/qs-case-study.git;
   cd qs-case-study
   ```

2. **建立映像並執行主程式:** 切換到專案目錄，並執行以下命令來建立Image和啟動API sercice：
   ```bash
   docker-compose up
   ```
    Docker compose 會自動建立image、啟動container和API 服務。如果想要背景執行，可以在command最後加入參數 `-d` 。

3. 將 .env 檔案中的 GA4 Measurement ID/API secret替換掉，並將 GCP 金鑰命名為`gcp_logging_key.json`，放置在專案資料夾中（與 main.py 相同目錄下）
    - Notice: 需開啟 Cloud logging 與 Measurement protocol 寫入權限

4. **確認正常啟動:** 執行上述命令後，應該會在terminal會看到 pytest 的測試結果，以及 API 正在監聽請求的訊息。如下圖：
    ![image](https://github.com/user-attachments/assets/1d073d74-57f8-4625-a3e9-1c28c5a75e7d)

## 測試 API

1. **Endpoint:** 此 API 提供單一功能來產生隨機顏色的png檔案：
   - **URL:** `http://localhost:9543/generate_png`
   - **Method:** GET
   - **參數:**
     - `width`: png 寬度。
     - `height`: png 高度。

2. **測試工具:** 可以直接使用瀏覽器如chrome訪問範例Endpoint (http://localhost:9543/generate_png?width=100&height=100)，或使用像 [Postman](https://www.postman.com/downloads/) 等工具進行測試，用 curl 的話也 ok，如：
      ```bash
       curl -o output.png "http://localhost:9543/generate_png?width=100&height=100"
      ```
