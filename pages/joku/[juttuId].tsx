import { useRouter } from 'next/router'

export default function Post() {
  const router = useRouter()
  const { juttuId, toinenId } = router.query;

  return  (
    <div>
        <h1>juttusivu</h1>
        <p>juttu id: {juttuId}</p>
        <p>toinen id: {toinenId}</p>
    </div>
  );
}