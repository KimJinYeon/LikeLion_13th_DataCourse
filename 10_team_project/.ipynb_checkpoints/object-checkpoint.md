{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c2cf085f",
   "metadata": {},
   "source": [
    "# 우리나라 10월부터 위드 코로나 해도 될까?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b91cbfe",
   "metadata": {},
   "source": [
    "## 코로나보드와 블룸버그 데이터 비교해보자"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e80a700",
   "metadata": {},
   "source": [
    "#### 위드 코로나 하는 국가들과 하지 않는 국가들의 수치는 얼마나 차이날까?\n",
    "\n",
    "* 위드 코로나 시행국가들은 Enough for % of people, fully vaccinated이 미시행 국가들보다 높을까?\n",
    "* 위드 코로나 시행국가들은 발생률, 위중증률, 치명률이 미시행 국가들보다 낮을까?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0003eb61",
   "metadata": {},
   "source": [
    "## 구체적인 국가 선정: 영국의 데이터 분석해보자"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8b30c5f",
   "metadata": {},
   "source": [
    "#### 영국은 위드 코로나를 어떻게 하고 있고, 어떤 영향이 있었을까?\n",
    "\n",
    "1. 영국의 코로나 대처 정책 탐구\n",
    "    * 신호등 시스템: red, ember, green system 분석\n",
    "    * 정말 추적식 방역을 포기했나?: 2021 f/w 방역계획서 분석\n",
    "    * 영국 국민들은 위드 코로나 정책에 얼마나 찬성할까?\n",
    "2. 영국의 데이터 수집 (2021-09-28일까지 누적 데이터)\n",
    "    * 검사 관련 지표 Testing\n",
    "        + 시간에 따라 검사 시행 횟수가 어떻게 변화했는지? -> 검사 시행이 늘어서 확진자가 증가한 것처럼 보일 수 있다.\n",
    "    * 발병 관련 지표 Cases\n",
    "        + 일일/누적 지표, 7일 단위 10만명당 발병률/추이\n",
    "    * 보건 관련 지표 Healthcare\n",
    "        + 코로나로 인한 입원 케이스, 코로나로 인한 환자, 음압병동 환자\n",
    "    * 백신 관련 지표 Vaccinations\n",
    "        + 1차/2차 접종률, 전체 접종률\n",
    "    * 사망 관련 지표 Deaths\n",
    "        + 양성판정 후 28일 이내 사망, 코로나로 인한 사망 증명서 포함된 케이스\n",
    "    * 자료 출처 : www.gov.uk\n",
    "3. 영국 데이터 기반으로 분석, 시각화\n",
    "    * 시간 범위: 위드 코로나 시행 시점~ 현재\n",
    "    * 자료 범위: 검사, 발병, 보건, 백신, 사망\n",
    "    * 위드 코로나 시행 날짜 기준으로 지표가 악화되었을까?\n",
    "        + 얼마나 발병, 보건, 사망 데이터에 영향이 있었을까?\n",
    "        + 위드 코로나 시행 전후로 검사 케이스에 크게 변화가 있었을까?\n",
    "        + 현재 영국의 지표는 어떨까?\n",
    "    * 위드 코로나 시행 날짜 기준으로 영국의 지표는 얼마나 좋았을까?\n",
    "        + 내가 직접 비교하지 말고 다른 팀원이 각자 모은 데이터와 비교 가능할 수 있게 모으자."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "297108a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
