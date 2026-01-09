# Social Backend API

"클라우드 커뮤니티" 서비스의 백엔드 API 서버를 구현합니다.

지난주에 각자 작성한 **REST API Docs**를 기반으로 실제 동작하는 서버를 개발합니다.

수행 방법에 대한 상세는 노션 페이지 내 과제 제출 페이지 (4주차 과제) 에서 확인해주세요!

## 📋 과제 수행 방법

### 1. 리포지토리 Fork하기

- 아래 명령어를 사용해서 이 리포지토리를 fork 해주세요.
- **Windows**는 반드시 **Git Bash**를 사용해주세요!!!!! PowerShell이나 CMD에서는 아래 명령어가 작동하지 않습니다.
- GitHub CLI(`gh`)가 설치되어 있지 않다면??? -> [GitHub CLI 설치 가이드](https://cli.github.com/)를 참고하세요.

  ```bash
  # 현재 로그인된 GitHub ID를 자동으로 가져와서 Fork
  GITHUB_ID=$(gh api user --jq '.login') && \
  gh repo fork ej31/aws13th-social-backend --org no-easy-days --fork-name aws13th-social-backend-${GITHUB_ID} && \
  gh repo clone no-easy-days/aws13th-social-backend-${GITHUB_ID} && \
  cd aws13th-social-backend-${GITHUB_ID}
  ```

### 2. 본인의 브랜치로 PR 올리기

- 본인의 GitHub ID가 포함된 브랜치로 PR을 제출해주세요.
- 프로젝트 내에는 종류 불문하고 어떠한 비밀번호도 절대 평문으로 저장하지 마세요!
- public repository에 키 잘못올리면 골치아파집니다!
- `.env` 파일은 `.gitignore`에 추가하여 Git에 커밋되지 않도록 하세요!


#### 작업 브랜치 목록
- 반드시 **본인의 GitHub ID가 포함된 브랜치**로 PR을 제출해주세요.
- PR은 `main` 브랜치를 base로 생성해주세요.
- 이 프로젝트에 미리 생성 된 브랜치 목록은 아래와 같습니다.

  ```
  developer/eunice.shin54
  developer/kjhappy77
  developer/0206pdh
  developer/unbi53
  developer/vocolate17
  developer/lee940609
  developer/ldj990517
  developer/huhsungwoo0609
  developer/mins8578
  developer/rlaehdrbs90
  developer/monghowol
  developer/kjsskkh01
  developer/seonjeongug2
  developer/100psk
  developer/youngwoo7804
  developer/jmw010314
  developer/dong.hee4881
  developer/lhj990118
  developer/jarvan44
  developer/dongq511
  developer/jeongmin7397
  developer/ywkim0201
  developer/ri2eeuntt
  ```

### 3. PR 제출 절차


#### PR 제목 작성 규칙
- `[본인ID] 기능 요약` 형식으로 작성
  - 예시: `[eunice.shin54] 회원가입 및 로그인 API 구현`
- 주기적으로 코드리뷰를 진행하기 위해서 PR을 자주 올려주세요! (현업에서 프로젝트 완성하듯이 진행됩니다!)
  - 코드리뷰를 통해 도출 된 내용을 계속 신경 써야 합니다. 과제 완성 후 한방에 쾅하고 PR 올리시면 안됩니다!

#### PR 본문 작성 가이드

PR 제출 시 아래 내용을 복사해서 PR 내용 본문에 사용해주세요!
- 체크박스는 "[x]" 와 같이 작성하면 체크가 된 채로 렌더링 됩니다. 아래 템플릿에는 비교를 위해 일부러 "[x]" 처리 했습니다. 실제로 쓰실 때는 모두 체크해서 제출해주시면 되겠습니다!


```markdown
**구현 목표**
- 이번 PR에서 구현한 주요 기능이나 목적

**구현 내용**
- API 엔드포인트 목록
- 주요 구현 사항 상세 설명

**기술적 의사결정**
- 프로젝트 구조 및 아키텍처 선택 이유
- 사용한 라이브러리/프레임워크 및 선택 근거

**보안 고려사항**
- 비밀번호 암호화 방식
- 인증/인가 처리 방법
- 기타 보안상 신경 쓴 부분

**테스트 완료 항목**
- [x] 모든 API 엔드포인트 테스트 완료
- [ ] Postman/curl로 정상 동작 확인
- [x] 에러 케이스 처리 확인
- [ ] .env 파일 gitignore 등록 확인

```

#### 제출 전 Self-Review 체크리스트!

- [ ] 코드에 주석이 적절히 작성되어 있는가?
- [ ] 불필요한 console.log, 디버깅 코드가 제거되었는가?
- [ ] .env 파일이 .gitignore에 포함되어 있는가?
- [ ] API 문서와 실제 구현이 일치하는가?
- [ ] 에러 핸들링이 적절히 구현되어 있는가?
- [ ] HTTP 상태 코드가 적절히 사용되었는가?

### 4. 커밋 메시지 작성 규칙
이번 과제에서는 커밋 컨벤션을 적용합니다!

현업에서 많이 사용하는 Conventional Commits 형식을 사용해주세요.

커밋은 의미있는 단위로 가능한 작게, 자주 등록해주세요!

큰 단위로 (뭉탱이로) 커밋하는 버릇들면 열심히 일한 티가 전혀 안납니다.

- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `refactor:` 코드 리팩토링
- `docs:` 문서 수정
- `test:` 테스트 코드 추가/수정
- `chore:` 빌드, 설정 파일 수정
- `wip:` 작업 중 임시 저장을 위해 커밋하는 경우




#### 예시
```
feat: 회원가입 API 구현
fix: 로그인 시 토큰 만료 검증 오류 수정
refactor: 사용자 인증 미들웨어 분리
```

## 📅 제출

- **제출 마감**: 2026.01.19 수업 시작 전
- **제출 방법**: 본 저장소를 Fork하여 작업 후 본인 github id의 브랜치에 PR 제출 할 것

