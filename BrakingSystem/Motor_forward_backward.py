{\rtf1\ansi\ansicpg1252\cocoartf1504
{\fonttbl\f0\fnil\fcharset0 Consolas;}
{\colortbl;\red255\green255\blue255;\red132\green134\blue132;\red38\green38\blue38;\red234\green234\blue234;
\red148\green6\blue75;\red14\green114\blue164;\red19\green36\blue126;}
{\*\expandedcolortbl;\csgray\c100000;\cssrgb\c58824\c59608\c58824;\cssrgb\c20000\c20000\c20000;\cssrgb\c93333\c93333\c93333;
\cssrgb\c65490\c11373\c36471;\cssrgb\c0\c52549\c70196;\cssrgb\c9412\c21176\c56863;}
\margl1440\margr1440\vieww14320\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
# author: Abu Chowdhury\cf3 \

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 # Class: IST 440W\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 # Year: Fall 2016\
# Group: Braking System\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 import\cf3  RPi.\cf6 GPIO\cf3  \cf5 as\cf3  \cf6 GPIO         #importing GPIO\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 from\cf3  time \cf5 import\cf3  sleep\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setmode(\cf6 GPIO\cf3 .\cf6 BOARD\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 Motor1A \cf5 =\cf3  \cf6 16    \cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 Motor1B \cf5 =\cf3  \cf6 18   #calling motor 1 setpoint\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 Motor1E \cf5 =\cf3  \cf6 22\
\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 Motor2A \cf5 =\cf3  \cf6 19\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 Motor2B \cf5 =\cf3  \cf6 21   #calling motor 2 set point\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 Motor2E \cf5 =\cf3  \cf6 23\cf3 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setup(Motor1A,\cf6 GPIO\cf3 .\cf6 OUT\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setup(Motor1B,\cf6 GPIO\cf3 .\cf6 OUT\cf3 ) #setting up the motor 1\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setup(Motor1E,\cf6 GPIO\cf3 .\cf6 OUT\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setup(Motor2A,\cf6 GPIO\cf3 .\cf6 OUT\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setup(Motor2B,\cf6 GPIO\cf3 .\cf6 OUT\cf3 ) #setting up the motor 2\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .setup(Motor2E,\cf6 GPIO\cf3 .\cf6 OUT\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 print\cf3 (\cf7 'Going forwards'\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1A,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1B,\cf6 GPIO\cf3 .\cf6 LOW\cf3 ) #motor 1 spinning forwards\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1E,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2A,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2B,\cf6 GPIO\cf3 .\cf6 LOW\cf3 )  motor 2 spinning forwards\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2E,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 sleep(\cf6 2\cf3 )  # wait\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 print\cf3 (\cf7 'Going backwards'\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1A,\cf6 GPIO\cf3 .\cf6 LOW\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1B,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 ) #mototr 1 starts moving backwards\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1E,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2A,\cf6 GPIO\cf3 .\cf6 LOW\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2B,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 ) #mototr 2 starts moving backwards\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2E,\cf6 GPIO\cf3 .\cf6 HIGH\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 sleep(\cf6 2\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 print\cf3 (\cf7 'Now stop'\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor1E,\cf6 GPIO\cf3 .\cf6 LOW\cf3 ) #mototr 1&2 stops\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .output(Motor2E,\cf6 GPIO\cf3 .\cf6 LOW\cf3 )\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf3 \
\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth1000\clftsWidth3 \clminw1000 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrs\brdrw20\brdrcf4 \clpadl200 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth18560\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadl200 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf0 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 GPIO\cf3 .cleanup() #cleanup the GPIO\cell \lastrow\row
}