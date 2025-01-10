*NAME:* SAMPANGI NAGAVARDHAN  
*COMPANY:* CODTECH IT SOLUTIONS  
*ID:* CT08DS540  
*DOMAIN:* Cyber Security and Ethical Hacking  
*DURATION:* December 2024 to January 2025  
## **Task 2: Web Application Vulnerability Scanner**

### **Description**
A Python tool to scan web applications for vulnerabilities such as SQL Injection and Cross-Site Scripting (XSS).

### **Features**
- Detects common vulnerabilities like SQL Injection and XSS.
- Parses web pages to analyze responses for potential flaws.

### **Requirements**
- Python 3.x
- `requests`
- `beautifulsoup4`

### **Setup**
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the script with the target URL.

### **Usage**
1. **SQL Injection Scan**:
   ```bash
   python vulnerability_scanner.py --sql "http://example.com/item?id=1"
   ```
2. **XSS Scan**:
   ```bash
   python vulnerability_scanner.py --xss "http://example.com/search?q="
   ```

### **Example**
```bash
python vulnerability_scanner.py --sql "http://example.com/item?id=1"
python vulnerability_scanner.py --xss "http://example.com/search?q="
```

---
