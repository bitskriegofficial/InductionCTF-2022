import express from "express";
import cors from "cors";

const app = express();
const PORT = 5000;

app.use(express.json())
app.use(cors())

app.get('/', (req, res) => {
    req.headers.password == 'android supremacy' ? res.send("BITSCTF{y0u_ar3_s0_c00l}") : res.send("Oombikko naaye");
  });

app.listen(PORT, () => {
    //console.log(`Server: http://localhost:${PORT}`);
    console.log("Waguan my Gggggggggggggggggggg");
});