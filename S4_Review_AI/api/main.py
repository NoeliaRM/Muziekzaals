from fastapi import FastAPI
import uvicorn
from controller import review_ctrl
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI(debug= True)

#cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#routs
app.include_router(review_ctrl.router)

#starts app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port =8000)



