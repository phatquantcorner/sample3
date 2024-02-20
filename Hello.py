# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/phatquantcorner/quantcorner_lseg_hackathon/main/dataset.csv'
df = pd.read_csv(url, index_col=0)
df = df.pivot(index = 'Date', columns = 'Symbol', values = 'Adj Close')
df = (np.log(df) - np.log(df.shift(1))).dropna()

import riskfolio as rp

# Building the portfolio object
port = rp.Portfolio(returns=df)

def run():
    st.set_page_config(
        page_title="Portopt",
        page_icon="🖥",
    )

    st.write(df)



if __name__ == "__main__":
    run()
