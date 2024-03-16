library(tidyverse)
library(caret)
setwd('..')
model <- readRDS("RangerFITwPatch.rds")

finalBoundarydf = expand.grid(winr = seq(0.4, 0.6, length.out=50), 
                              pbr = seq(0, 1, length.out=50), 
                              KDA = seq(1, 5, length.out=50), 
                              Role = "SUPPORT", 
                              `Role %` = seq(0.1,1, length.out=20), 
                              Patch=c(1:12), 
                              Class = c("Mage", "Support"))

finalBoundarydf$Tier <- predict(model, finalBoundarydf)