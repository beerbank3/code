# iptables 명령어

1. drop ip 갯수 확인
- sudo iptables -L INPUT -n --line-numbers | grep DROP

2. drop ip순서대로 정렬
- sudo iptables -L INPUT -n --line-numbers | grep DROP | awk '{print $5}' | sort

3. 중복 drop ip 제거
- sudo iptables -L INPUT -n --line-numbers | grep DROP | awk '{print $5}' | sort | uniq

4. 정책 제거 
- iptables -D INPUT {number}